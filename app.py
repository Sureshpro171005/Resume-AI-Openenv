import gradio as gr
from env.resume_env import ResumeEnv

env = ResumeEnv(task="medium")

def run_optimizer():
    try:
        state = env.reset()
        initial = state["current_score"]

        steps = []
        actions = [
            "Add relevant skills",
            "Improve experience",
            "Optimize keywords"
        ]

        for action in actions:
            state, _, _, _ = env.step(action)
            steps.append(f"{action} → Score: {state['current_score']:.3f}")

        return (
            str(initial),
            str(state["current_score"]),
            "\n".join(steps),
            state["resume"]
        )

    except Exception as e:
        return (
            "Error",
            "Error",
            f"Error: {str(e)}",
            "Error"
        )


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Resume Optimization Agent")

    # OUTPUT SECTION FIRST
    initial = gr.Textbox(label="Initial Score")
    final = gr.Textbox(label="Final Score")
    steps = gr.Textbox(label="Steps Taken")
    resume = gr.Textbox(label="Optimized Resume", lines=10)

    # BUTTON AT BOTTOM
    btn = gr.Button("Generate 🚀")

    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, steps, resume]
    )

demo.launch()