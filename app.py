import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from .env")
    return api_key


def ask_gemini(client, question: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question,
    )

    output = getattr(response, "text", None)
    if output is None:
        raise ValueError("Gemini response did not include text output.")

    print("\nGemini:")
    print(output)
    return output


def main() -> None:
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)
    question = input("Ask Gemini: ")
    ask_gemini(client, question)


if __name__ == "__main__":
    main()