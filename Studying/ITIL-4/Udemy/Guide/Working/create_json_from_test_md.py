import json
import re

def process_markdown(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    letter_choice_pattern = r"^- ([A-D])\) (.+?)(?: \((Correct|Incorrect)\))?:$"
    tests = []
    current_test = None
    current_question = None
    explanation_buffer = None

    choice_regex = r"^- ([A-D])\)\s*(.*)$"  # Original choice pattern

    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith("# "):  # Correctly identifies test header
            test_number = re.search(r"#\s*Test\s*(\d+)", line).group(1)
            current_test = {"test_number": test_number, "questions": []}
            tests.append(current_test)

        elif line.startswith("## "):  # Correctly identifies question header

            if explanation_buffer:  # Check if there's an explanation pending assignment
                assign_explanation(current_question, explanation_buffer)
                explanation_buffer = None
            matches = re.search(r"##\s*Question\s*(\d+):\s*(Incorrect|Correct)", line)
            question_number, status = matches.groups()
            current_question = {
                "question_number": question_number,
                "status": status,
                "question_text": "",
                "choices": []
            }
            current_test["questions"].append(current_question)

        elif current_question and (line.startswith("**Which") or line.startswith("**Identify")):
            current_question["question_text"] = line.strip("**")

        elif line.startswith("- "):  # Correctly identify choice lines

            if explanation_buffer:  # Assign pending explanation if available
                assign_explanation(current_question, explanation_buffer)
                explanation_buffer = None

            choice_letter, choice_text = re.match(letter_choice_pattern, line).groups()
            is_correct, user_response = "(Correct)" in choice_text, "(Incorrect)" in choice_text
            choice_text = re.sub(r" \(\w+\)", "", choice_text)  # Remove (Correct)/(Incorrect) tags
            current_question["choices"].append({
                "choice": choice_letter,
                "text": choice_text,
                "is_correct": is_correct,
                "user_response": user_response,
                "explanation": ""  # Placeholder for an explanation
            })
        match = re.match(choice_regex, line)

        if match:  # Now we make sure the match is successful before proceeding
            choice_letter, choice_text = match.groups()
            is_correct, user_response = "(Correct)" in choice_text, "(Incorrect)" in choice_text
            choice_text = re.sub(r" \(\w+\)", "", choice_text)  # Clean the choice text
            current_question["choices"].append({
                "choice": choice_letter,
                "text": choice_text.strip(),  # Ensure we strip any trailing spaces
                "is_correct": is_correct,
                "user_response": user_response,
                "explanation": ""  # Placeholder for explanation
            })

        elif line.startswith(">"):
            explanation_buffer = line.strip("> ").strip()

        # Final check to assign any lingering explanation after all lines are processed
    if explanation_buffer:
        assign_explanation(current_question, explanation_buffer)

    # Final check to assign pending explanations omitted for brevity...
    return {"tests": tests}

def assign_explanation(current_question, explanation_text):
    """
    Assigns the explanation text to the last choice of the current question.
    """
    if current_question and current_question["choices"]:
        last_choice = current_question["choices"][-1]
        last_choice["explanation"] = explanation_text

def save_json(data, output_path):
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    markdown_file = "Review_Guide.md"
    json_data = process_markdown(markdown_file)
    output_file = "output.json"
    save_json(json_data, output_file)
    print(f"JSON file saved as {output_file}")

if __name__ == "__main__":
    main()
