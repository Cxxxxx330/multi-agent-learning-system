class AgentOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent("Planner")
        self.tutor = TutorAgent("Tutor")
        self.evaluator = EvaluatorAgent("Evaluator")
        self.memory = MemoryAgent()

    def run(self, goal: str):
        session_id = str(uuid.uuid4())
        print(f"\n🚀 Session: {session_id}")
        print(f"🎯 Goal: {goal}\n")

        # Step 1: 任务拆解
        tasks = self.planner.run(goal)
        print("📅 学习计划:", tasks)

        results = []
