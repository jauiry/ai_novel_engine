from openai import OpenAI

client = OpenAI(
    api_key="sk-cp-9CmALoHnkNiWXUKtGUg5ibzYPuVSZjk9vWo1Pz2g0PaPYlBKogu2IcNjVExGv5BLHj-fAqGRH3TM17D0csUB1AFRGvWdhdOlLD-vo4ZJCwDGDOYkIqw-c4o",
    base_url="https://api.minimax.chat/v1"
)

def ask_minimax(prompt):

    completion = client.chat.completions.create(
        model="MiniMax-M2.5",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return completion.choices[0].message.content