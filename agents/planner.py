class PlannerAgent(BaseAgent):
    def run(self, goal: str, context=None) -> List[str]:
        prompt = f"""
        你是学习规划专家，请将目标拆解为每日学习任务：
        目标：{goal}
        要求：输出结构化步骤（Day1, Day2...）
        """
        result = call_llm(prompt)

        # 简化处理（真实情况需解析结构化输出）
        tasks = [f"Task {i+1}" for i in range(5)]
        return tasks
