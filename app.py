import gradio as gr
from env.resume_env import ResumeEnv

env = ResumeEnv(task="medium")

def run_optimizer(resume_text, job_desc):
    env = ResumeEnv(task="medium")

    # ✅ Inject user inputs into environment
    env.resume = resume_text
    env.job_description = job_desc

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
        steps.append(f"Step {i+1}: {action} → Score: {state['current_score']:.3f}")

    final = state["current_score"]
    improvement = (final - initial) * 100

    return (
        f"{initial:.3f}",
        f"{final:.3f} ({improvement:+.2f}%)",
        "\n".join(steps),
        state["resume"]
    )

# 🎨 UI DESIGN
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🤖 AI Resume Optimization Agent")
    gr.Markdown("Improve your resume step-by-step using AI.")

    with gr.Row():
        with gr.Column():
            resume_input = gr.Textbox(
                label="📄 Your Resume",
                placeholder="Paste your resume here...",
                lines=10
            )

        with gr.Column():
            job_input = gr.Textbox(
                label="💼 Job Description",
                placeholder="Paste job description...",
                lines=10
            )

    btn = gr.Button("🚀 Optimize Resume", variant="primary")

    with gr.Row():
        initial = gr.Textbox(label="Initial Score")
        final = gr.Textbox(label="Final Score")
        improvement = gr.Textbox(label="Improvement")

    steps = gr.Textbox(label="📊 Optimization Steps", lines=8)
    output_resume = gr.Textbox(label="✨ Optimized Resume", lines=10)

    btn.click(
        fn=run_optimizer,
        inputs=[resume_input, job_input],
        outputs=[initial, final, improvement, steps, output_resume]
    )

demo.launch()