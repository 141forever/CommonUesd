import pdb
import sys
import os
import time
import json
import requests
import copy

import openai
from openai import OpenAI
import anthropic

# official o1
try:
    client = OpenAI(api_key="sk-proj-")
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content
    print(text)
except Exception as e:
    print(e)

# official claude
claude_client = anthropic.Anthropic(api_key='sk-ant-')
try:
    response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
except Exception as e:
    print(e)
