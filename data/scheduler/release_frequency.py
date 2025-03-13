class ReleaseFrequency:
    frequency_table = r"""
| Repository   | Release Type   | Approx. Monthly Code Change | Monthly Issues/Bugs | Contributors | Release Frequency (days) |
|--------------|----------------|-----------------------------|---------------------|--------------|---------------------------|
| Repo1        | Stable Release | 1.43% churn                 | 36 bugs             | 80           | 21                        |
| Repo2        | Stable Release | 1.60% churn                 | 32 bugs             | 50           | 28                        |
| Repo3        | Stable Release | 2.50% churn                 | 38 bugs             | 80           | 60                        |
| Repo4        | Stable Release | 2.00% churn                 | 30 bugs             | 150          | 90                        |
| Repo5        | Stable Release | 2.67% churn                 | 27 bugs             | 150          | 45                        |
| Repo6        | Stable Release | 3.00% churn                 | 33 bugs             | 160          | 50                        |
| Repo7        | Stable Release | 8% churn                    | 54 bugs             | 180          | 100                       |
| Repo8        | Stable Release | 10% churn                   | 63 bugs             | 1200         | 120                       |
| Repo9        | Stable Release | 12% churn                   | 75 bugs             | 900          | 120                       |
| Repo10       | Stable Release | 4% churn                    | 36 bugs             | 500          | 42                        |
| Repo11       | Stable Release | 15% churn                   | 80 bugs             | 1500         | 150                       |
"""
    instruction_template = (
        "Using the following additional context and table:\n\n"
        "Additional Context:\n{additional_context}\n\n"
        "Table:\n{table}\n\n"
        "Answer the following question based on the optimal release frequency observed in the table:\n\n"
        "Question: {question}\n"
        "Answer:"
    )
    additional_context = """
   If the question asks about healthcare, military or government code, provide a higher number of days for stability and compliance testing.
"""
    def getInstructionTemplate(self):
        return self.instruction_template
    def getFrequencyTable(self):
        return self.frequency_table
    def getAdditionalContext(self):
        return self.additional_context
    