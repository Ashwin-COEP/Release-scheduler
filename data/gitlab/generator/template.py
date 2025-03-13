import re
class GeneratorTemplate:
    gitlabjobtemplate = r"""
    {user-provided or "scratch"}:
      image: {user provided or "scratch"}
      script:
    {Commands given by the user. If unspecified, "echo 'Hello'"}
      variables:
        KUBERNETES_CPU_REQUEST: {provided}
        KUBERNETES_CPU_LIMIT: {provided}
        KUBERNETES_MEMORY_REQUEST: {provided}
        KUBERNETES_MEMORY_LIMIT: {provided}
"""
    instruction_template = (
    "Using the following additional context and GitLab job YAML syntax:\n\n"
    "Additional Context:\n{additional_context}\n\n"
    "Syntax:\n{gitlabjobtemplate}\n\n"
    "Generate a GitLab job based on the template :\n\n"
    "Question: {question}\n"
    "Answer:"
)
    # Function to fill missing values in the question
    # Default values
    DEFAULT_VALUES = {
        "KUBERNETES_CPU_REQUEST": "0.5",
        "KUBERNETES_CPU_LIMIT": "1",
        "KUBERNETES_MEMORY_REQUEST": "512Mi",
        "KUBERNETES_MEMORY_LIMIT": "1Gi"
    }
    def fill_missing_question_values(self,question: str) -> str:
        lower_question = question.lower()

        assumptions = []

        if not re.search(r"cpu request|cpu requests|requires cpus|", lower_question):
            assumptions.append(f"Assuming {self.DEFAULT_VALUES['KUBERNETES_CPU_REQUEST']} KUBERNETES_CPU_REQUEST")
        if not re.search(r"max cpu|cpu max|cpu limit", lower_question):
            assumptions.append(f"Assuming {self.DEFAULT_VALUES['KUBERNETES_CPU_LIMIT']} KUBERNETES_CPU_LIMIT")
        if not re.search(r"memory request|RAM request|requires RAM", lower_question):
            assumptions.append(f"Assuming {self.DEFAULT_VALUES['KUBERNETES_MEMORY_REQUEST']} KUBERNETES_MEMORY_REQUEST")
        if not re.search(r"max RAM|max memory|maximum memory", lower_question):
            assumptions.append(f"Assuming {self.DEFAULT_VALUES['KUBERNETES_MEMORY_LIMIT']} KUBERNETES_MEMORY_LIMIT")

        if assumptions:
            question += " " + " ".join(assumptions)
        
        return question
    # Todo
    additional_context = """
"""
    def getGeneratorTemplate(self):
        return self.gitlabjobtemplate
    def getInstructionTemplate(self):
        return self.instruction_template
    def getAdditionalContext(self):
        return self.getAdditionalContext