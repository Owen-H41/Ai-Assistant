import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types




def main():
    parser = argparse.ArgumentParser(description="Ai Code Assistant")
    parser.add_argument("user_prompt", type=str, help="type query for the Ai Assistant here")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RunTimeError("no api key")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)
    
    if response.usage_metadata == None:
        raise RunTimeError("API requst failure likely")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    
    print(response.text)


if __name__ == "__main__":
    main()
