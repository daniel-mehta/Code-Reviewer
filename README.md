# 🔍 Code Reviewer — LLM-Powered Code Review Tool
![Python](https://img.shields.io/badge/python-3.8-blue)
![Built with Jupyter](https://img.shields.io/badge/built%20with-Jupyter-orange)
![Made with VS Code](https://img.shields.io/badge/made%20with-VS%20Code-1f425f.svg)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![DeepSeek Coder](https://img.shields.io/badge/Model-DeepSeek--Coder-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Status: MVP](https://img.shields.io/badge/status-MVP-yellow)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)




A local, terminal-based code review assistant using open-source LLMs like `deepseek-coder` via [Ollama](https://ollama.com).

> 🛠️ Built in a single afternoon as a quick way to learn and implement Ollama with pre-trained local LLMs — fast, focused, and functional.

---

## Features

- 🧾 Loads and analyzes `.py` or `.txt` code files
- 🤖 Reviews powered by `deepseek-coder` running locally (via Ollama)
- 📝 Outputs structured markdown:
  - `## Summary`
  - `## Issues`
  - `## Suggestions`
- 💾 Optionally saves to `.md` for sharing or documentation
- 🔁 Modular design with selectable review modes

---

## 🧠 Why?

Traditional linters focus on syntax and formatting. This tool provides **high-level feedback** on logic, clarity, and structure — in seconds.

Great for:
- Practicing clean code
- Reviewing your own scripts before a PR
- Learning what makes readable, maintainable code

---

## 🚀 Quickstart

### 1. Install Ollama

Follow the instructions at [ollama.com/download](https://ollama.com/download)

Then pull the model:

```bash
ollama run deepseek-coder
```

### 2. Clone this repo
```bash
git clone https://github.com/daniel-mehta/Code-Reviewer
cd Code-Reviewer
```

### 3. Run it
```bash
python reviewer.py
```
Follow the prompts to:
- Select a file
- Choose a review mode
- Save the output (or just print it)
---
## 🗂 Project Structure
```bash
code-reviewer/
├── reviews/             # Saved markdown reviews
├── sample_scripts/      # Test code files
├── utils.py             # File loading, prompt building, saving
├── reviewer.py          # LLM call, review pipeline, CLI logic
├── prototype.ipynb      # Prototype notebook (initial dev/testing)
└── README.md            # You're here
```
---
## 🧪 Example Output
```bash
## Summary
Defines a recursive factorial function and a greeting function. Prints the result of both.

## Issues
- No input validation for negative values in factorial
- Lacks docstrings or clear comments
- greet() uses string concatenation instead of f-string

## Suggestions
- Add input validation for edge cases
- Use `f"hello {name}"` for readability
- Include comments/docstrings for clarity
```
---
## 🧩 Modes
- **default** — general, practical suggestions
- **beginner_friendly** — simplified explanations for newer devs
- **strict** — senior dev style, focused on maintainability and performance
---
## 🌱 Future Ideas
- Batch-review folders (*.py)
- Live web frontend with file upload (WIP)
---
## 🛠 Built With
- Python 3.8.5
- Ollama
- deepseek-coder
- Jupyter Notebook (prototype phase)
- Visual Studio Code
---
## 📄 License
MIT — free to use, modify, or extend.

---
## ✍️ Notes
This project was built entirely in an afternoon to quickly explore the power of running local LLMs with Ollama.

