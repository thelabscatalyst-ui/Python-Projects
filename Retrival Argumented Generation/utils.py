"""
Utilities for the RAG course labs.
Uses Groq (free, no credit card) via the OpenAI-compatible client.

Setup:
  1. Sign up free at https://console.groq.com
  2. Create an API key there
  3. Paste it in the .env file next to this script:
       GROQ_API_KEY=your_key_here
"""

import os
from typing import Dict, List, Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_together_key() -> str:
    # Now reads GROQ_API_KEY instead of Together.ai
    key = os.environ.get("GROQ_API_KEY", "")
    if not key:
        raise EnvironmentError(
            "GROQ_API_KEY not set. "
            "Sign up free at https://console.groq.com, create an API key, "
            "then add it to the .env file as:  GROQ_API_KEY=your_key_here"
        )
    return key


def get_proxy_url() -> str:
    return "https://api.groq.com/openai/v1"


def get_proxy_headers() -> Dict[str, str]:
    return {}


def _get_client():
    from openai import OpenAI
    return OpenAI(
        api_key=get_together_key(),
        base_url=get_proxy_url(),
    )


def generate_with_single_input(
    prompt: str,
    max_tokens: int = 512,
    model: str = "llama-3.1-8b-instant",
    role: str = "user",
    together_api_key: Optional[str] = None,
) -> Dict[str, str]:
    """
    Send a single prompt to the LLM and return a dict with 'role' and 'content'.

    Parameters
    ----------
    prompt : str
        The text to send.
    max_tokens : int
        Maximum tokens in the response.
    model : str
        Together.ai model identifier.
    role : str
        The role to assign the prompt ('user' or 'assistant').
    together_api_key : str, optional
        Override the key from the environment.
    """
    if together_api_key:
        os.environ["TOGETHER_API_KEY"] = together_api_key

    client = _get_client()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": role, "content": prompt}],
        max_tokens=max_tokens,
    )
    msg = response.choices[0].message
    return {"role": msg.role, "content": msg.content}


def generate_with_multiple_input(
    messages: List[Dict[str, str]],
    max_tokens: int = 512,
    model: str = "llama-3.1-8b-instant",
    together_api_key: Optional[str] = None,
) -> Dict[str, str]:
    """
    Send a conversation (list of role/content dicts) to the LLM.

    Parameters
    ----------
    messages : list of dict
        Each dict must have 'role' and 'content' keys.
    max_tokens : int
        Maximum tokens in the response.
    model : str
        Together.ai model identifier.
    together_api_key : str, optional
        Override the key from the environment.
    """
    if together_api_key:
        os.environ["TOGETHER_API_KEY"] = together_api_key

    client = _get_client()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
    )
    msg = response.choices[0].message
    return {"role": msg.role, "content": msg.content}
