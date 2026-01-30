import tiktoken

enc  = tiktoken.encoding_for_model("gpt-4o")
texts = "hey there, my name is sahil"
token = enc.encode(texts)

print("Tokens", token)

decode = enc.decode(token)
print("Decode", decode)