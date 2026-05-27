from ollama import chat

stream = chat(model="gemma4:e4b",messages=[
    {
        "role":"system",
        "content":"You are a senior Python developer."
    },
    {
        "role":"user",
        "content":"Write a function that takes as arguments 2 integers and returns the first integer modulo the second."
    }],
    stream=True
    )

for chunk in stream:
    print(chunk["message"]["content"], end ="", flush=True)