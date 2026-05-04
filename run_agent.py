import os
from dotenv import load_dotenv
from src.agent import HealthCoachAgent

if __name__ == "__main__":
    load_dotenv()
    user_id = "user001"
    location = "San Francisco"
    agent = HealthCoachAgent(user_id, location)
    agent.run()
