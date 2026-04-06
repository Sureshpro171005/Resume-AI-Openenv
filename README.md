# Resume AI OpenEnv

## Overview

This project is an AI environment where an agent improves resumes to better match job descriptions.
It simulates a real-world task of resume optimization using step-based actions and reward feedback.

---

## Features

* OpenEnv compatible (`reset`, `step`)
* Reward-based learning environment
* Semantic similarity scoring (resume vs job)
* 3 difficulty levels (easy → medium → hard)
* Interactive UI using Gradio

---

## Environment Design

### Observation Space

* Resume text
* Job description
* Current similarity score

### Action Space

* Add relevant skills
* Improve experience section
* Optimize keywords for ATS
* Rewrite summary professionally

### Reward Function

* Reward = change in similarity score
* Range: 0 → 1
* Positive reward → better alignment
* Negative reward → worse alignment

---

## Tasks

### Easy

* Basic skill matching
* Short resume + simple job

### Medium

* Skills + experience optimization
* Moderate job description

### Hard

* Full resume improvement
* Complex AI/ML job description

---

## How It Works

1. Environment loads resume + job description
2. Agent selects an action
3. Resume is modified
4. Similarity score is recalculated
5. Reward is given based on improvement

---

## Run Locally

```bash
pip install -r requirements.txt
python inference.py
```

---

## Deploy (Local UI)

```bash
python app.py
```

---

## Project Structure

```
resume-ai-openenv/
│
├── env/
├── tasks/
├── inference.py
├── app.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Future Improvements

* LLM-powered resume rewriting
* Reinforcement learning agent
* Real job dataset integration
* Multi-step optimization tracking

---

