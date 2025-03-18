import os
from dotenv import load_dotenv
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner, set_default_openai_client, exceptions
from pydantic import BaseModel
import asyncio
from openai import AsyncOpenAI

load_dotenv()

custom_client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
set_default_openai_client(custom_client)

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
    model="gpt-4o-mini",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
    model="gpt-4o-mini",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
    model="gpt-4o-mini",
)


async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
    model="gpt-4o-mini",
)

async def main():
    print("\n=== Testing Homework ===")
    result = await Runner.run(triage_agent, "As a part of my homework, I need to understand how Britishers entered India.")
    print(f"Response:\n{result.final_output}\n")

    print("=== Testing Non-Homework Question ===")
    try:
        result = await Runner.run(triage_agent, "what is life")
        print(f"Response:\n{result.final_output}\n")
    except exceptions.InputGuardrailTripwireTriggered as e:
        print(f"Guardrail triggered: {e}")

if __name__ == "__main__":
    asyncio.run(main())