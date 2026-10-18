import ollama
model="llama3:latest"

msgs=[
    {
        "role":"system",
        "content":"Friendly Assistant,Try giving reponses as short as possible"
    }
]

while True:
    u_prompt=input("Enter your prompt : ")
    u_role={"role":"user","content":u_prompt}
    msgs.append(u_role)
    response=ollama.chat(model=model,messages=msgs)
    res=response.message.content
    print("Assistant : ",res)
    assistant_role={"role":"assistant","content":res}
    msgs.append(assistant_role)