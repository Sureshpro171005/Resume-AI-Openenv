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
        "Optimize keywords",
        "Rewrite summary professionally"
    ]

    for i, action in enumerate(actions):
        state, reward, done, _ = env.step(action)
        steps.append(f"[STEP {i}] {action} → Score: {state['current_score']:.3f}")

    return (
        str(initial),
        str(state["current_score"]),
        "\n".join(steps),
        state["resume"]
    )

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Resume Optimization Agent")

    btn = gr.Button("Generate 🚀")

    initial = gr.Textbox(label="Initial Score")
    final = gr.Textbox(label="Final Score")
    steps = gr.Textbox(label="Steps")
    resume = gr.Textbox(label="Optimized Resume", lines=10)

    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, steps, resume]
    )

demo.launch()