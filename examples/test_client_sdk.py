import os
from hybrid_edge import HybridLLM
from dotenv import load_dotenv

# Load secrets for testing
load_dotenv() 

# 1. Initialize the Library
ai = HybridLLM(
    username="YOUR_GITHUB_USERNAME",  # Hardcode or load from env
    gist_id=os.getenv("GIST_ID"),
    secret_key=os.getenv("SECRET_KEY")
)

# 2. Use it!
print("--------------------------------")
print("Sending prompt to home GPU...")
answer = ai.generate("Explain Quantum Physics in 1 sentence.")

print(f"Answer: {answer}")
print("--------------------------------")