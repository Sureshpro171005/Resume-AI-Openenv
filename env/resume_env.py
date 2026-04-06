import json
import random
from env.utils import calculate_similarity


class ResumeEnv:

    def __init__(self, task="easy"):
        self.task = task
        self.data = self.load_task(task)

    def load_task(self, task):
        with open(f"tasks/{task}.json") as f:
            return json.load(f)

    def reset(self):
        # ✅ Use user input if provided
        if hasattr(self, "resume") and hasattr(self, "job_description"):
            self.job = self.job_description
        else:
            sample = random.choice(self.data)
            self.resume = sample["resume"]
            self.job = sample["job_description"]

        # ✅ Calculate initial score
        self.score = calculate_similarity(self.resume, self.job)

        return {
            "resume": self.resume,
            "job_description": self.job,
            "current_score": self.score
        }

    def step(self, action):
        old_score = self.score

        # ✅ Simulate AI improvements
        if "skills" in action.lower():
            self.resume += " Python Machine Learning AI"
        elif "experience" in action.lower():
            self.resume += " Built real-world ML projects"
        elif "keywords" in action.lower():
            self.resume += " data analysis NLP deep learning"
        else:
            self.resume += " professional summary updated"

        # ✅ Recalculate score
        new_score = calculate_similarity(self.resume, self.job)

        reward = new_score - old_score
        self.score = new_score

        
        return {
            "resume": self.resume,
            "job_description": self.job,
            "current_score": self.score
        }, reward, False, {}