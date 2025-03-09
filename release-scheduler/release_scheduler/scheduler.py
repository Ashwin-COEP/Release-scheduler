import sys

sys.path.append("./")
from auth import authenticator
from data.scheduler import release_frequency
from env.env import Env
import requests

class Scheduler:
    def query_model(self, prompt: str, headers):
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200, "temperature": 0.2}}
        env = Env()
        response = requests.post(env.API_URL, headers=headers, json=payload)
        return response.json()
    def GetSchedule(self):
        authenticator_instance = authenticator.Authenticator()
        auth_header = authenticator_instance.getAuthenticationHeader()
        headers = {}
        headers.update(auth_header)
        scheduler_instance = release_frequency.ReleaseFrequency()
        frequency_table = scheduler_instance.getFrequencyTable()
        instruction_template = scheduler_instance.getInstructionTemplate()
        question = input("Enter your question about optimal release frequency: ")
        prompt = instruction_template.format(
            additional_context=scheduler_instance.getAdditionalContext(),
            table=frequency_table,
            question=question
        )
        result = self.query_model(prompt,headers)
        if isinstance(result, list) and result:
            print("\nAnswer:", result[0].get("generated_text", "").strip())
        else:
            print("\nAnswer:", result.get("generated_text", "").strip())