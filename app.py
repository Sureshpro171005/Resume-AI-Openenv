import gradio as gr
import matplotlib.pyplot as plt
from env.resume_env import ResumeEnv

env = ResumeEnv(task="medium")


def run_optimizer():
    try:
        state = env.reset()
        initial_score = state["current_score"]

        scores = [initial_score]
        steps = []

        actions = [
            "Add relevant skills",
            "Improve experience",
            "Optimize keywords"
        ]

        for action in actions:
            state, _, _, _ = env.step(action)
            scores.append(state["current_score"])
            steps.append(f"✔ {action} → {state['current_score']:.3f}")

        final_score = state["current_score"]
        improvement = (final_score - initial_score) * 100

        # Graph
        plt.figure()
        plt.plot(scores, marker='o')
        plt.title("Score Improvement")
        plt.xlabel("Steps")
        plt.ylabel("Score")
        plt.grid()

        path = "graph.png"
        plt.savefig(path)
        plt.close()

        return (
            f"{initial_score:.3f}",
            f"{final_score:.3f}",
            f"+{improvement:.1f}%",
            "\n".join(steps),
            state["resume"],
            path
        )

    except Exception as e:
        return ("Error", "Error", "Error", str(e), "Error", None)


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    #  HEADER
    gr.Markdown(
        """
        # 🚀 AI Resume Optimizer  
        ### Turn your resume into a job-winning profile using AI
        """
    )

    #  SCORE CARDS
    with gr.Row():
        initial = gr.Textbox(label="📊 Initial Score")
        final = gr.Textbox(label="📈 Final Score")
        improvement = gr.Textbox(label="🚀 Improvement %")

    #  STEPS CARD
    with gr.Group():
        gr.Markdown("### ⚙️ Optimization Steps")
        steps = gr.Textbox(lines=4)

    #  RESUME CARD
    with gr.Group():
        gr.Markdown("### 📄 Optimized Resume")
        resume = gr.Textbox(lines=8)

    #  GRAPH CENTERED
    with gr.Row():
        graph = gr.Image(label="📊 Score Improvement")

    gr.Markdown("---")

    #  BUTTON
    btn = gr.Button("🚀 Optimize Resume", variant="primary")

    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, improvement, steps, resume, graph]
    )

demo.launch()