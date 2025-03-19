import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_default_openai_client, set_default_openai_api, set_tracing_disabled
import asyncio
from providers.azure_openai import get_azure_openai_client, get_azure_openai_reasoning_client

load_dotenv()

# Get OpenAI client using Azure OpenAI provider
openai_client = get_azure_openai_reasoning_client()

# Set the default OpenAI client for the Agents SDK
set_default_openai_client(openai_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


async def main():

    # Use the correct model name format for Azure OpenAI
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=os.getenv("O3_MINI_DEPLOYMENT")
    )

    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print("\nAgent response:\n")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())