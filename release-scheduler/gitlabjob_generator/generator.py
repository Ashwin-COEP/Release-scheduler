import sys

sys.path.append("./")
from auth import authenticator
from data.gitlab.generator.template import GeneratorTemplate
from env.env import Env
import requests

class Generator:
    def query_model(self, prompt: str, headers):
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200, "temperature": 0.2}}
        env = Env()
        response = requests.post(env.StarCoder_API_URL, headers=headers, json=payload)
        return response.json()
    def GenerateJob(self):
        authenticator_instance = authenticator.Authenticator()
        auth_header = authenticator_instance.getAuthenticationHeader()
        headers = {}
        headers.update(auth_header)
        generator_instance = GeneratorTemplate()
        job = generator_instance.getGeneratorTemplate()
        instruction_template = generator_instance.getInstructionTemplate()
        question = input("Enter details of the GitLab job: ")
        question = generator_instance.fill_missing_question_values(question)
        prompt = instruction_template.format(
            additional_context=generator_instance.getAdditionalContext(),
            gitlabjobtemplate=job,
            question=question
        )
        result = self.query_model(prompt,headers)
        if isinstance(result, list) and result:
            print("\nAnswer:", result[0].get("generated_text", "").strip())
        else:
            print("\nAnswer:", result.get("generated_text", "").strip())