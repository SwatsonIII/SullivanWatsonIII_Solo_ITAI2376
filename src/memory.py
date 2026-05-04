class AgentMemory:
    def __init__(self):
        self.history = []

    def add_entry(self, data):
        self.history.append(data)

    def get_recent(self, n=3):
        return self.history[-n:]
