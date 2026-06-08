"""
Ungraded Lab 2: LLM Calls and Crafting Simple Augmented Prompts
================================================================
Run this file directly:  python Basic_concepts_RAG.py

Requirements:
  pip install openai python-dotenv

Set your Together.ai API key in a .env file next to this script:
  TOGETHER_API_KEY=your_key_here
"""

from utils import (
    generate_with_single_input,
    generate_with_multiple_input,
    get_proxy_url,
    get_proxy_headers,
    get_together_key,
)

# ---------------------------------------------------------------------------
# Section 1.1 – generate_with_single_input
# ---------------------------------------------------------------------------
print("=" * 60)
print("Section 1.1 – Single-input call")
print("=" * 60)

output = generate_with_single_input(prompt="What is the capital of France?")
print("Role:", output["role"])
print("Content:", output["content"])

# ---------------------------------------------------------------------------
# Section 1.2 – generate_with_multiple_input (conversation)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("Section 1.2 – Multi-turn conversation call")
print("=" * 60)

messages = [
    {"role": "user",      "content": "Hello, who won the FIFA world cup in 2018?"},
    {"role": "assistant", "content": "France won the 2018 FIFA World Cup."},
    {"role": "user",      "content": "Who was the captain?"},
]

output = generate_with_multiple_input(messages=messages, max_tokens=100)
print("Role:", output["role"])
print("Content:", output["content"])

# ---------------------------------------------------------------------------
# Section 1.3 – Direct OpenAI client (Together.ai is OpenAI-compatible)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("Section 1.3 – Direct OpenAI client against Together.ai")
print("=" * 60)

from openai import OpenAI

client = OpenAI(
    api_key=get_together_key(),
    base_url=get_proxy_url(),
)

response = client.chat.completions.create(
    messages=messages,
    model="llama-3.1-8b-instant",
    max_tokens=100,
)
print(response.choices[0].message.content)

# ---------------------------------------------------------------------------
# Section 2 – Augmented / RAG-style prompt
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("Section 2 – Integrating data into an LLM prompt (RAG demo)")
print("=" * 60)

house_data = [
    {
        "address": "123 Maple Street",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 1500,
        "price": 230000,
        "year_built": 1998,
    },
    {
        "address": "456 Elm Avenue",
        "city": "Shelbyville",
        "state": "TN",
        "zip": "37160",
        "bedrooms": 4,
        "bathrooms": 3,
        "square_feet": 2500,
        "price": 320000,
        "year_built": 2005,
    },
]


def house_info_layout(houses):
    layout = ""
    for house in houses:
        layout += (
            f"House located at {house['address']}, {house['city']}, "
            f"{house['state']} {house['zip']} with "
            f"{house['bedrooms']} bedrooms, {house['bathrooms']} bathrooms, "
            f"{house['square_feet']} sq ft area, priced at ${house['price']}, "
            f"built in {house['year_built']}.\n"
        )
    return layout


def generate_prompt(query, houses):
    houses_layout = house_info_layout(houses)
    prompt = f"""
Use the following houses information to answer users queries.
{houses_layout}
Query: {query}
"""
    return prompt


print("\n-- Layout preview --")
print(house_info_layout(house_data))

query = "What is the most expensive house? And the bigger one?"

print("\n-- WITHOUT house info (LLM answers from its own knowledge) --")
result_no_context = generate_with_single_input(prompt=query, role="user")
print(result_no_context["content"])

print("\n-- WITH house info (augmented / RAG-style prompt) --")
augmented_prompt = generate_prompt(query, houses=house_data)
result_with_context = generate_with_single_input(
    prompt=augmented_prompt, role="user", max_tokens=300
)
print(result_with_context["content"])
