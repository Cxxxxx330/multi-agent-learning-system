class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__("MemoryAgent")
        self.memory_store = []

    def update(self, record: Dict):
        self.memory_store.append(record)

    def retrieve(self, k=3):
        return self.memory_store[-k:]
