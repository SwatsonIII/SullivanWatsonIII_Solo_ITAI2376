from langchain.llms import OpenAI
import os
from .tools import get_health_data, get_weather
from .memory import AgentMemory

class HealthCoachAgent:
    def __init__(self, user_id, location):
        self.user_id = user_id
        self.location = location
        self.memory = AgentMemory()
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)
    
    def perceive(self):
        health_data = get_health_data(self.user_id)
        weather = get_weather(self.location)
        perception = {**health_data, **weather}
        self.memory.add_entry({"perception": perception})
        return perception

    def reason(self, perception):
        # Use a reasoning pattern: Chain of Thought
        context = f"""
        User health data: heart rate {perception['heart_rate']}, steps {perception['steps_today']}, 
        sleep {perception['sleep_hours']:.1f}h, mood {perception['mood']}.
        Weather: {perception['temp_c']:.1f}°C, {perception['condition']}.
        Recent memory: {self.memory.get_recent()}
        """
        prompt = (
            f"{context}\n"
            "As a health coach, analyze the user's current state and suggest a specific, encouraging next action "
            "to improve their health, considering their habits and the weather."
        )
        response = self.llm(prompt)
        self.memory.add_entry({"reasoning": prompt, "response": response})
        return response

    def act(self, recommendation):
        print(f"Coach Recommendation: {recommendation}")

    def run(self):
        perception = self.perceive()
        recommendation = self.reason(perception)
        self.act(recommendation)
