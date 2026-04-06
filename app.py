import gradio as gr
from env.resume_env import ResumeEnv

env = ResumeEnv(task="medium")

def run_optimizer():
    state = env.reset()
    initial = state["current_score"]

    steps = []
    actions = [
        "Add relevant skills",
        "Improve experience",
        "Optimize keywords"
    ]

    for action in actions:
        state, reward, _ = env.step(action)
        steps.append(f"{action} → Score: {state['current_score']:.3f}")

    return initial, state["current_score"], "\n".join(steps), state["resume"]

demo = gr.Interface(
    fn=run_optimizer,
    inputs=[],
    outputs=[
        gr.Text(label="Initial Score"),
        gr.Text(label="Final Score"),
        gr.Text(label="Steps"),
        gr.Textbox(label="Optimized Resume", lines=10)
    ],
    title=" AI Resume Optimization Agent"
)

demo.launch()