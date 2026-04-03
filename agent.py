import json
import os

from strands import Agent
from strands.models.ollama import OllamaModel

from subfunctions.profile_prompter import run_profile_prompter

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="granite4:3b",
)

agent = Agent(model=ollama_model)


def profile():
    username = input("Letterboxd Username :")

    try:
        markdown_content = run_profile_prompter(username)
    except Exception as e:
        print(f"Error generating markdown content: {e}")
        return

    try:
        response = agent(markdown_content)
        print("Agent response:")
        print(response)

        response_content = str(response)

        try:
            profile_json = json.loads(response_content)
            os.makedirs("cache/json", exist_ok=True)
            output_path = f"cache/json/{username}.json"
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(profile_json, json_file, indent=4)
            print(f"\nProfile saved to {output_path}")

        except json.JSONDecodeError as e:
            print("Error: The agent's response is not valid JSON.")
            print(f"Error details: {e}")

            os.makedirs("cache/json", exist_ok=True)
            output_path = f"cache/json/{username}_response.json"
            with open(output_path, "w", encoding="utf-8") as json_file:
                json_file.write(response_content)
            print(f"Raw response saved to {output_path}")

    except Exception as e:
        print(f"Error sending content to the agent: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    profile()
