from openai import OpenAI

client = OpenAI()

def call_llm(system_prompt, user_prompt, temperature=0.2):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
