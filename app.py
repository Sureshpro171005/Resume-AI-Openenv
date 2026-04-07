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

        # 📊 Create graph
        plt.figure()
        plt.plot(scores, marker='o')
        plt.title("Score Improvement")
        plt.xlabel("Steps")
        plt.ylabel("Score")
        plt.grid()

        graph_path = "score.png"
        plt.savefig(graph_path)
        plt.close()

        return (
            f"{initial_score:.3f}",
            f"{final_score:.3f} (+{improvement:.1f}%)",
            "\n".join(steps),
            state["resume"],
            graph_path
        )

    except Exception as e:
        return (
            "Error",
            "Error",
            f"Error: {str(e)}",
            "Error",
            None
        )


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("## 🤖 AI Resume Optimization Agent")
    gr.Markdown("Automatically improves resume using AI actions")

    #   clean UI
    

    # 📊 Outputs
    initial = gr.Textbox(label="📊 Initial Score")
    final = gr.Textbox(label="📈 Final Score (with improvement)")
    steps = gr.Textbox(label="⚙️ Steps Taken", lines=4)
    resume = gr.Textbox(label="✅ Optimized Resume", lines=8)
    graph = gr.Image(label="📊 Score Improvement Graph")

    btn = gr.Button("🚀 Optimize Resume")
    btn.click(
        fn=run_optimizer,
        inputs=[],
        outputs=[initial, final, steps, resume, graph]
    )

demo.launch()