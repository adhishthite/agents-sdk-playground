import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_default_openai_client, set_default_openai_api, set_tracing_disabled
import asyncio
from openai import AsyncAzureOpenAI, AsyncOpenAI

load_dotenv()


# Create OpenAI client using Azure OpenAI
openai_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
)

# Set the default OpenAI client for the Agents SDK
set_default_openai_client(openai_client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


async def main():

    # Use the correct model name format for Azure OpenAI
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    )

    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print("\nAgent response:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())