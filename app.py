import gradio as gr
import matplotlib.pyplot as plt
import os
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
            state, reward, done = env.step(action)
            scores.append(state["current_score"])
            steps.append(f"✔ {action} → {state['current_score']:.3f}")

        final_score = state["current_score"]
        improvement = (final_score - initial_score) * 100

        #  Explanation
        explanation = """✔ Added relevant skills
✔ Improved experience clarity
✔ Matched job keywords"""

        # 📊 Graph
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
            f"{final_score:.3f}  (+{improvement:.1f}%)",
            "\n".join(steps),
            state["resume"],
            explanation,
            path
        )

    except Exception as e:
        return (
            "Error",
            "Error",
            str(e),
            "Error",
            "Error",
            None
        )


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    #  HEADER
    gr.Markdown(
        """
        # 🚀 AI Resume Optimizer  
        ### Smart AI agent that improves your resume step-by-step
        """
    )

    #  SCORE CARDS
    with gr.Row():
        initial = gr.Textbox(label="📊 Initial Score")
        final = gr.Textbox(label="📈 Final Score")

    #  STEPS
    gr.Markdown("### ⚙️ Optimization Steps")
    steps = gr.Textbox(lines=4, show_label=False)

    #  RESUME
    gr.Markdown("### 📄 Optimized Resume")
    resume = gr.Textbox(lines=8, show_label=False)

    #  WHY IMPROVED
    gr.Markdown("### 💡 Why Score Improved")
    explain = gr.Textbox(lines=3, show_label=False)

    #  GRAPH
    gr.Markdown("---")
    graph = gr.Image(label="📊 Score Improvement", height=400)

    #  BUTTON
    gr.Markdown("---")
    btn = gr.Button("🚀 Optimize Resume", variant="primary")

    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, steps, resume, explain, graph]
    )

port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)