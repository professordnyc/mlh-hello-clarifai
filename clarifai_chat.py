import os
import sys
from dotenv import load_dotenv

# Set HOME environment variable for Windows if not set
if sys.platform.startswith('win') and 'HOME' not in os.environ:
    os.environ['HOME'] = os.environ.get('USERPROFILE', '')

# Now import Clarifai after setting environment variables
from clarifai.client import Model

# Load environment variables from .env file
load_dotenv()

def chat_with_llama(prompt, system_message="You are a helpful assistant."):
    """
    Send a prompt to a free Clarifai model and return the response.
    
    Args:
        prompt (str): The user's message/prompt
        system_message (str): System message to set the assistant's behavior
        
    Returns:
        The model's response or error message
    """
    try:
        # Using Llama-3 model from Clarifai with correct API format
        model = Model("https://clarifai.com/meta/Llama-3/models/Llama-3_2-3B-Instruct")
        
        # Format the prompt for the Llama-3 model
        # Using a simpler format that works with the Clarifai SDK
        formatted_prompt = f"""[INST] <<SYS>>
        {system_message}
        <</SYS>>
        
        {prompt} [/INST]"""
        
        try:
            # The predict method expects a string input for this model
            response = model.predict_by_bytes(
                formatted_prompt.encode(),
                input_type="text"
            )
            
            # Return the text response
            if response and hasattr(response, 'outputs') and len(response.outputs) > 0:
                output = response.outputs[0]
                if hasattr(output, 'data') and hasattr(output.data, 'text'):
                    return output.data.text
                return str(output)  # Fallback to string representation
                    
        except Exception as e:
            # If predict_by_bytes fails, try the regular predict method
            try:
                response = model.predict(formatted_prompt)
                if response and hasattr(response, 'outputs') and len(response.outputs) > 0:
                    output = response.outputs[0]
                    if hasattr(output, 'data') and hasattr(output.data, 'text'):
                        return output.data.text
                    return str(output)  # Fallback to string representation
            except Exception as inner_e:
                raise inner_e  # Re-raise the inner exception if both methods fail
        return "Error: No response from the model"
        
    except Exception as e:
        error_msg = f"Error calling Clarifai API: {str(e)}"
        print(f"\n{error_msg}")
        return error_msg

def main():
    """Example usage of the Clarifai Llama 3 chat function."""
    try:
        print("Clarifai Llama 3 Chat")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            print("\nAssistant: ", end="", flush=True)
            response = chat_with_llama(
                prompt=user_input,
                system_message="You are a helpful assistant. Keep responses concise and informative."
            )
            if response:
                print(f"{response}\n")
            else:
                print("Sorry, I encountered an error processing your request.\n")
            
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
