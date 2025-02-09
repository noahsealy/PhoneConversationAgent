from query_processing import ask_once, interactive_chat

def handle_customer_inquiry():
    # Example of using ask_once for a single response
    customer_question = "What are the store hours?"
    system_prompt = """You are a friendly phone agent for a retail store. 
    Our store hours are 9 AM to 9 PM Monday through Saturday, 
    and 10 AM to 6 PM on Sundays."""
    
    response = ask_once(customer_question, system_prompt)
    print(f"\nCustomer: {customer_question}")
    print(f"Agent: {response}")

def start_customer_service_chat():
    # Example of using interactive_chat for a conversation
    system_prompt = """You are a helpful customer service agent for a retail store.
    You are friendly and professional. You can help with:
    - Store hours (9 AM to 9 PM Mon-Sat, 10 AM to 6 PM Sun)
    - Product availability
    - Returns and exchanges
    - General inquiries
    Always maintain a professional tone and sign off with 'Is there anything else I can help you with?'"""
    
    print("Customer Service Chat Started (type 'quit' to exit)")
    chat_history = interactive_chat(system_prompt)
    return chat_history

if __name__ == "__main__":
    # Example of using both functions
    print("\n=== Single Question Example ===")
    handle_customer_inquiry()
    
    print("\n=== Interactive Chat Example ===")
    start_customer_service_chat()
