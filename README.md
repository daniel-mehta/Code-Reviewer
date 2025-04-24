# 🔍 Code Reviewer — LLM-Powered Code Review Tool
![Python](https://img.shields.io/badge/python-3.8-blue)
![Built with Jupyter](https://img.shields.io/badge/built%20with-Jupyter-orange)
![Streamlit UI](https://img.shields.io/badge/UI-Streamlit-red)
![Made with VS Code](https://img.shields.io/badge/made%20with-VS%20Code-1f425f.svg)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![DeepSeek Coder](https://img.shields.io/badge/Model-DeepSeek--Coder-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Status: MVP](https://img.shields.io/badge/status-MVP-yellow)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)




A local, terminal-based code review assistant using open-source LLMs like `deepseek-coder` via [Ollama](https://ollama.com).

> 🛠️ Backend built in a single afternoon to explore local LLMs with Ollama — the Streamlit frontend came a few days later for a smoother review experience.

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
- 🖥️ Web UI with Streamlit for file upload and output preview
- 🔘 Dropdown to choose review mode (default, beginner, strict)
- ✅ Checkbox to save markdown review



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

### 4. Front End

Prefer using a web interface instead of the terminal?

Install Streamlit (if you haven't yet)
```bash
pip install streamlit
```

Run the Streamlit app:
```bash
streamlit run app.py
```
Then:
- Upload a .py or .txt file
- Select a review mode (default, beginner_friendly, strict)
- View structured markdown output in your browser
- Optionally save the review to /reviews

> 📄 See Code Reviewer PDF.pdf for a sample output & UI preview
> 📸 Example UI Output (see below)
---
## 🗂 Project Structure
```bash
code-reviewer/
├── reviews/             # Saved markdown reviews
├── sample_scripts/      # Test code files
├── utils.py             # File loading, prompt building, saving
├── reviewer.py          # Core logic (prompt, review, model)
├── app.py               # Streamlit UI
├── prototype.ipynb      # Initial dev/testing
├── README.md            # You're here
└── Code Reviewer PDF.pdf # Example UI + output

```
---
## 📸 Screenshot

![Code Reviewer PDF_page-0001](https://github.com/user-attachments/assets/563cc821-2347-483d-a960-87026b100072)

---
## 🧪 Example Output (Terminal Version)
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
- Streamlit
---
## 📄 License
MIT — free to use, modify, or extend.

---
## ✍️ Notes
This project was built entirely in an afternoon to quickly explore the power of running local LLMs with Ollama.

