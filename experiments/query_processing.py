from openai import OpenAI
from env_utils import get_env_value

# Initialize the client with your API key
client = OpenAI(api_key=get_env_value('OPENAI_API_KEY'))

def ask_once(question, system_prompt="You are a helpful, friendly AI assistant."):
    """Single question and answer with GPT"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content

def interactive_chat(system_prompt="You are a helpful, friendly AI assistant."):
    """Interactive chat session with history"""
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                break
                
            messages.append({"role": "user", "content": user_input})
            
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            print("\nAI:", ai_response)
            
            messages.append({"role": "assistant", "content": ai_response})
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    
    return messages  # Returns the conversation history

if __name__ == "__main__":
    print("Start chatting (type 'quit' to exit)")
    interactive_chat()