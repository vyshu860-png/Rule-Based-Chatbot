print ("welcome to the Rule_Based_Chatbot")
name=input("enter the name")
print("hello",name)
message=input("you:  ")
message=message.lower()
if message=="hello":
    print("Bot:  Hi !  how are you.")
elif message=="hi":
    print("Bot:Hello! ,nice to meet you.")
elif message =="help":
    print("Bot: I can answer greetings and basic questions.")
elif message =="what is an ai":
    print("Bot: ai stands for Artificial Intelligence.")
elif message =="Thanks bye":
    print("Bot: ok good bye!")
else:
    print("Bot: sorry,I don't  understand.")
    
    