"""
AI Research Agent - Project 1 (Gemini version, retry)
--------------------------------------------------------
Run:
    python research_agent_gemini.py "your question here"
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

MODEL = "gemini-3.1-flash-lite"

SYSTEM_PROMPT = """You are a careful research assistant. When you answer:
1. Use Google Search grounding to find current, relevant information.
2. Base every claim on what you find - do not rely on prior knowledge for facts that could be outdated.
3. Produce a final report in this exact format:

## Summary
(2-4 sentence overview)

## Key Findings
- Finding one [source: domain.com]
- Finding two [source: domain.com]

## Sources
1. Title - URL
2. Title - URL

Keep the report focused. Do not pad it."""


def run_research(question: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            #tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    return response.text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python research_agent_gemini.py "your question"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    print(f"Researching: {question}\n")
    report = run_research(question)
    print(report)