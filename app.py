import gradio as gr
from env.resume_env import ResumeEnv


def run_optimizer(resume_text, job_text):
    # Create environment
    env = ResumeEnv(task="medium")

    # Inject user input
    env.resume = resume_text
    env.job_description = job_text

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

    final_score = state["current_score"]
    improvement = (final_score - initial) * 100

    return (
        f"{initial:.3f}",
        f"{final_score:.3f} ({improvement:+.2f}%)",
        "\n".join(steps),
        state["resume"]
    )


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Resume Optimization Agent")

    # 🔥 INPUTS
    resume_input = gr.Textbox(
        label="Paste Your Resume",
        lines=6,
        placeholder="Enter your resume content here..."
    )

    job_input = gr.Textbox(
        label="Job Description",
        lines=6,
        placeholder="Paste job description here..."
    )

    btn = gr.Button("Generate 🚀")

    # 🔥 OUTPUTS
    initial = gr.Textbox(label="Initial Score")
    final = gr.Textbox(label="Final Score (+ improvement %)")
    steps = gr.Textbox(label="Steps Taken")
    resume = gr.Textbox(label="Optimized Resume", lines=10)

    # 🔗 CONNECT BUTTON
    btn.click(
        fn=run_optimizer,
        inputs=[resume_input, job_input],
        outputs=[initial, final, steps, resume]
    )


demo.launch()