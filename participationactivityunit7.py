prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)