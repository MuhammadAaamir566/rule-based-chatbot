# ============================================
# Rule-Based AI Chatbot - DecodeLabs Project 1
# ============================================

# STEP 1: Knowledge Base (Dictionary)
# Key = user ka sawaal, Value = chatbot ka jawab
responses = {
    "hello"     : "Hi there! How can I help you?",
    "hi"        : "Hello! Nice to meet you!",
    "how are you" : "I am just a bot, but I am doing great!",
    "what is ai"  : "AI stands for Artificial Intelligence!",
    "bye"       : "Goodbye! Have a great day!",
    "help"      : "I can answer basic questions. Try saying hello!",
    "name"      : "My name is DecoBot, your AI assistant!"
}

# STEP 2: Chatbot Start
print("=" * 40)
print("   Welcome to DecoBot!")
print("   Type 'quit' to exit")
print("=" * 40)

# STEP 3: Infinite Loop (Chatbot ka Heartbeat)
while True:
    
    # User se input lo
    raw_input_text = input("You: ")
    
    # STEP 4: Sanitization (Clean karo input)
    clean_input = raw_input_text.lower().strip()
    
    # STEP 5: Exit Command check karo
    if clean_input == "quit":
        print("DecoBot: Goodbye! See you next time!")
        break
    
    # STEP 6: Dictionary se jawab dhundho
    # .get() method: agar key mile toh uski value,
    # warna default message
    reply = responses.get(clean_input, "I don't understand. Try 'help'!")
    
    print("DecoBot:", reply)