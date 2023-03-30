import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message)
