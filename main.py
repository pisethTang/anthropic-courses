
import sys 

from dotenv import load_dotenv
import os 


# anthropic config 
load_dotenv()

claude_model: str = os.getenv("CLAUDE_MODEL", "")
anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")


assert claude_model, "Error: CLAUDE_MODEL cannot be empty. Update .env"
assert anthropic_api_key, "ERROR: ANTHROPIC_API_KEY cannot be empty. Update .env"



def main():
    claude_service = Claude(model=claude_model)




if __name__ == "__main__":
    if sys.platform == "win32":
        