import json
import random
import string
import os

def random_name():
    first = ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()
    last = ''.join(random.choices(string.ascii_lowercase, k=7)).capitalize()
    return f"{first} {last}"

def random_email(i):
    return f"testuser{i}@beta.dev"

def generate_agent(i):
    return {
        "id": f"agent_{i}",
        "name": random_name(),
        "email": random_email(i),
        "password": "Test1234!",
        "role": random.choice(["explorer", "commentator", "creator", "trader", "networker"]),
        "timezone": random.choice(["America/New_York", "Europe/London", "Asia/Tokyo"]),
        "interests": random.sample(["crypto", "ai", "sports", "news", "music", "economics"], k=2)
    }

def main():
    agents = [generate_agent(i) for i in range(1, 55720)]
    
    # Get the directory of the current script and build path to data folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(script_dir), "data")
    output_file = os.path.join(data_dir, "agent_profiles.json")
    
    with open(output_file, "w") as f:
        json.dump(agents, f, indent=2)
    print(f"✅ Generated {len(agents)} agent profiles.")

if __name__ == "__main__":
    main()