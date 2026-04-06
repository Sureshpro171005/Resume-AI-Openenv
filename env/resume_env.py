import gradio as gr
from env.resume_env import ResumeEnv


def run_optimizer():
    env = ResumeEnv(task="medium")

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
        state, reward, done = env.step(action)
        steps.append(f"Step {i+1}: {action} → Score: {state['current_score']:.3f}")

    final = state["current_score"]
    improvement = (final - initial) * 100

    return (
        f"{initial:.3f}",
        f"{final:.3f}",
        f"{improvement:+.2f}%",
        "\n".join(steps),
        state["resume"]
    )


# 🎨 CLEAN PROFESSIONAL UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🤖 AI Resume Optimization Agent")
    gr.Markdown("Click the button to see how AI improves a resume step-by-step.")

    btn = gr.Button("🚀 Generate Optimization", variant="primary")

    with gr.Row():
        initial = gr.Textbox(label="📊 Initial Score")
        final = gr.Textbox(label="📈 Final Score")
        improvement = gr.Textbox(label="📉 Improvement")

    steps = gr.Textbox(label="⚙️ Optimization Steps", lines=8)
    output_resume = gr.Textbox(label="✨ Optimized Resume", lines=10)

    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, improvement, steps, output_resume]
    )

demo.launch()