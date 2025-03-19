import os
from openai import AsyncAzureOpenAI
from dotenv import load_dotenv

def get_azure_openai_client():
    """
    Creates and returns an Azure OpenAI client instance.
    
    Returns:
        AsyncAzureOpenAI: Configured Azure OpenAI client
    """
    load_dotenv()
    
    return AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )

def get_azure_openai_reasoning_client():
    """
    Creates and returns an Azure OpenAI reasoning client instance.
    
    Returns:
        AsyncAzureOpenAI: Configured Azure OpenAI reasoning client
    """

    load_dotenv()
    
    return AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_REASONING_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_REASONING_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_REASONING_ENDPOINT"),
    )