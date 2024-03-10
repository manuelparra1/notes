import re
import json


def process_markdown(markdown_file):
    tests = []
    current_test = None
    current_question = None
    current_choices = []

    with open(markdown_file, "r") as file:
        for line in file:
            if line.startswith("# Test"):
                if current_test is not None:
                    tests.append(current_test)
                current_test = {"test_number": int(line.split()[-1]), "questions": []}
                current_question = None
                current_choices = []
            elif line.startswith("## Question"):
                if current_question is not None:
                    current_test["questions"].append(current_question)
                current_question = {
                    "question_number": line.split()[2][:-1],
                    "status": line.split()[-1],
                    "choices": [],
                }
            elif line.startswith("**Question Text**"):
                current_question["question_text"] = next(file).strip()
            elif line.startswith("**Explanation**"):
                next(file)  # skip the next line
                for _ in range(4):
                    choice_line = next(file)
                    choice = choice_line.split()[0][:-1]
                    choice_text = choice_line.split()[1:]
                    current_choices.append(
                        {
                            "choice": choice,
                            "text": " ".join(choice_text),
                            "explanation": next(file).strip(),
                        }
                    )
                current_question["choices"] = current_choices

    if current_test is not None:
        tests.append(current_test)

    return tests


def save_json(data, output_file):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    markdown_file = "Review_Guide.md"
    json_file = "review_guide.json"

    data = process_markdown(markdown_file)
    save_json(data, json_file)
