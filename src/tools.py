import random

# Tool 1: Simulate retrieving user health data from wearables
def get_health_data(user_id):
    # Mocked data for demo
    return {
        "heart_rate": random.randint(60, 110),
        "steps_today": random.randint(2000, 12000),
        "sleep_hours": random.uniform(5.5, 8.5),
        "mood": random.choice(["happy", "tired", "stressed", "motivated"])
    }

# Tool 2: Simulate getting weather data
def get_weather(location):
    # Mocked data for demo
    return {
        "temp_c": random.uniform(10, 30),
        "condition": random.choice(["sunny", "rainy", "cloudy", "windy"])
    }
