def load_code(filepath):
    """Reads the contents of a code file as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return ""
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return ""

def build_prompt(code, mode="default"):
    """Constructs a code review prompt with markdown-style sections."""
    
    if mode == "default":
        instructions = """
You are a code reviewer. Read the following code and respond in markdown with three sections:

## Summary
Briefly explain what this code does.

## Issues
List any problems, inefficiencies, or bad practices you notice.

## Suggestions
Recommend improvements, refactors, or best practices.

Respond directly below each section header in clear, concise language.
"""
    elif mode == "beginner_friendly":
        instructions = """
You are a friendly code reviewer helping a beginner programmer.

Respond in markdown with three sections:
## What the Code Does
## Things to Improve
## Suggestions and Tips

Be kind and explain anything that might be confusing for a new coder.
"""
    elif mode == "strict":
        instructions = """
You're a senior software engineer performing a detailed and critical code review.

Be blunt. Use markdown headers:

## Code Summary
## Technical Issues
## Required Changes

Focus on performance, logic errors, maintainability, and standards compliance.
"""
    else:
        raise ValueError(f"Unknown review mode: {mode}")

    prompt = f"{instructions.strip()}\n\n```python\n{code.strip()}\n```"
    return prompt


def save_review(text, path):
    """Saves the review text to the specified markdown or text file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Review saved to: {path}")
    except Exception as e:
        print(f"❌ Failed to save review: {e}")