import gradio as gr
from env.resume_env import ResumeEnv

env = ResumeEnv(task="medium")

def run_optimizer(user_resume, user_job):
    try:
        # Override env data with user input
        env.resume = user_resume
        env.job = user_job

        # Initial score
        initial_score = env.score = env.score = env.score = env.score = env.score = 0
        initial_score = env.score = env.score = env.score = env.score = env.score = 0

        initial_score = env.score = env.score = env.score = env.score = env.score = 0

        initial_score = env.score = env.score = env.score = env.score = env.score = 0

        initial_score = env.score = env.score = env.score = env.score = env.score = 0

        # Proper calculation
        state = {
            "resume": user_resume,
            "job_description": user_job,
            "current_score": env.score
        }

        from env.utils import calculate_similarity
        initial_score = calculate_similarity(user_resume, user_job)
        env.score = initial_score

        steps = []

        actions = [
            "Add relevant skills",
            "Improve experience",
            "Optimize keywords"
        ]

        for action in actions:
            state, _, _, _ = env.step(action)
            steps.append(f"✔ {action} → {state['current_score']:.3f}")

        final_score = state["current_score"]

        improvement = ((final_score - initial_score) * 100)

        return (
            f"{initial_score:.3f}",
            f"{final_score:.3f}  (+{improvement:.1f}%)",
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


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("## 🤖 AI Resume Optimization Agent")
    gr.Markdown("Improve your resume automatically using AI")

    # INPUT SECTION
    with gr.Group():
        resume_input = gr.Textbox(
            label="📄 Paste Your Resume",
            placeholder="Enter your resume here...",
            lines=6
        )

        job_input = gr.Textbox(
            label="💼 Job Description",
            placeholder="Paste job description here...",
            lines=6
        )

    generate_btn = gr.Button("🚀 Optimize Resume")

    # OUTPUT SECTION
    with gr.Group():
        initial = gr.Textbox(label="📊 Initial Score")
        final = gr.Textbox(label="📈 Final Score (with improvement)")
        steps = gr.Textbox(label="⚙️ Steps Taken", lines=4)
        optimized = gr.Textbox(label="✅ Optimized Resume", lines=8)

    generate_btn.click(
        fn=run_optimizer,
        inputs=[resume_input, job_input],
        outputs=[initial, final, steps, optimized]
    )

demo.launch()