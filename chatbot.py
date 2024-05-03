class Restuarantchatbot:
    def __init__(self):
        self.greetings=["Hello There How are You","welcome to our restuarant"]
        self.menu=["1.vadapav, 2.bhel, 3panipuri"]
        self.goodbye=["Thanks For Visiting","Bye byee"]
        self.unknown=["I Couldnot understand","Please enter your message again"]

    def greet(self):
        return self.greetings[0]
    
    def say_goodbye(self):
        return self.goodbye[0] 
    
    def provide_menu(self):
        return self.menu[0]
    
    def reservation(self):
        return "reservation available currently"
    
    def respond(self,message):
        message=message.lower()
        if "reservation" in message:
            return self.reservation()
        
        elif "menu" in message:
            return self.provide_menu()
        
        elif "bye" in message:
            return self.say_goodbye()
        
        elif any(word in message for word in ["hii","hello","hey"]):
            return self.greet()
        
        else:
            return self.unknown[0]
        
chatbot=Restuarantchatbot()
print("Restuarant chatbot: "+chatbot.greet())
while True:
    user_input=input("You: ")
    if user_input.lower() == "exit":
        print(chatbot.say_goodbye()) 

    response= chatbot.respond(user_input)
    print("Restuarant chatbot: "+ response)



    
    

    

        

