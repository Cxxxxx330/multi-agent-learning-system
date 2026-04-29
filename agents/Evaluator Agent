class EvaluatorAgent(BaseAgent):
    def run(self, task: str, context=None) -> Dict:
        prompt = f"""
        针对该学习任务生成3道测试题，并附答案：
        {task}
        """
        response = call_llm(prompt)

        return {
            "questions": response,
            "score": 80  # 模拟评分
        }
