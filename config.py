import os
from dotenv import load_dotenv
import google.generativeai as genai

def configure_env():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key = api_key)
        print("API KEY loaded successfully")
    else:
        raise ValueError("Missing API Key")
    
