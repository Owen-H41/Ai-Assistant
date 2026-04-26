import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_function import available_functions
from call_function import call_function


def main():
    parser = argparse.ArgumentParser(description="Ai Code Assistant")
    parser.add_argument("user_prompt", type=str, help="type query for the Ai Assistant here")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RunTimeError("no api key")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    
    if response.usage_metadata == None:
        raise RunTimeError("API requst failure likely")
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls == None:
        print(response.text)
    else:
        function_results = []
        for item in response.function_calls:
            function_call_result = call_function(item, verbose=False)
            if len(function_call_result.parts) == 0:
                raise Exception("no parts in function call result")
            if function_call_result.parts[0].function_response == None:
                raise Exception("function_response is missing")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("function_response.response is missing")
            function_results.append(function_call_result.parts[0])
            if args.verbose == True:
                print(f"-> {function_call_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
