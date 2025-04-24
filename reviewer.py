import ollama
import os
from utils import load_code, build_prompt, save_review

def call_model(prompt, model="deepseek-coder"):
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = ollama.chat(model=model, messages=messages)
    return response["message"]["content"]

def review_code(filepath, mode="default", save=False):
    """Runs the full review pipeline for a given code file."""
    print("🔍 Loading code...")
    code = load_code(filepath)
    if not code:
        return "❌ No code loaded. Exiting."
    
    print("🧠 Building prompt...")
    prompt = build_prompt(code, mode)
    
    print("🤖 Sending to DeepSeek-Coder...")
    review = call_model(prompt, model="deepseek-coder")
    
    if save:
        filename = os.path.basename(filepath).replace(".py", "").replace(".txt", "")
        output_path = f"reviews/{filename}_review.md"
        save_review(review, output_path)
    
    return review

def user_input():
    """Collects user input for code review — filepath, mode, and save toggle."""
    filepath = input("Enter the path to the code file (e.g., sample scripts/test1.py): ").strip()
    
    mode = input("Choose review mode [default / beginner_friendly / strict] (default): ").strip()
    if mode == "":
        mode = "default"
    
    save_response = input("Save review to markdown file? [y/N]: ").strip().lower()
    save = save_response == "y"
    
    return filepath, mode, save

if __name__ == "__main__":
    filepath, mode, save = user_input()
    result = review_code(filepath, mode, save)
    
    print("\n📝 Review Output:\n")
    print(result)

def run_review(code_str, mode="default"):
    """Streamlit to call — builds prompt and returns LLM output."""
    prompt = build_prompt(code_str, mode)
    return call_model(prompt, model="deepseek-coder")
