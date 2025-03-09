import os
from dotenv import load_dotenv
class Authenticator:
    def getAuthenticationHeader(self):
        load_dotenv()
        api_token = os.getenv("HF_API_TOKEN")
        return {"Authorization": f"Bearer {api_token}"}