import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

import os

# Access environment variables
AZURE_OAI_KEY = os.getenv("AZURE_OAI_KEY")
AZURE_OAI_ENDPOINT = os.getenv("AZURE_OAI_ENDPOINT")
AZURE_OAI_MODEL = os.getenv("AZURE_OAI_MODEL")

code = '''
#include <stdio.h>

int main(){
    print("Hello World")
    return 0
}
'''

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = AZURE_OAI_ENDPOINT
openai.api_version = "2023-03-15-preview"
openai.api_key = AZURE_OAI_KEY

# Send request to Azure OpenAI model
print("Sending request for summary to Azure OpenAI endpoint...\n\n")
response = openai.ChatCompletion.create(
    engine=AZURE_OAI_MODEL,
    temperature=0.7,
    max_tokens=300,
    messages=[
       {"role": "system", "content": "You are a helpful assistant. Please suggest ways to improve this code."},
        {"role": "user", "content": code}
    ]
)

print("Summary: " + response.choices[0].message.content + "\n")