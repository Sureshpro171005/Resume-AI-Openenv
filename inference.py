from env.resume_env import ResumeEnv

actions = [
    "Add relevant skills from job description",
    "Improve experience with measurable impact",
    "Optimize keywords for ATS",
    "Rewrite summary professionally"
]

env = ResumeEnv(task="hard")

state = env.reset()

print("[START]")
print(f"Initial Score: {state['current_score']:.4f}")

for i, action in enumerate(actions):
    state, reward, _ = env.step(action)

    print(f"[STEP {i}]")
    print(f"Action: {action}")
    print(f"Reward: {reward:.4f}")
    print(f"Score: {state['current_score']:.4f}")

print("[END]")