class TutorAgent(BaseAgent):
    def run(self, task: str, context=None) -> str:
        prompt = f"""
        请讲解以下学习任务，并提供示例：
        {task}
        """
        return call_llm(prompt)
