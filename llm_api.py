
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
    return text
except Exception as e:
    print(e)
