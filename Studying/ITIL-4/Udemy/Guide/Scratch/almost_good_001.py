import re
import json


def markdown_to_json(markdown_file):
    with open(markdown_file, "r") as f:
        content = f.read()

    tests = []
    test_sections = re.findall(r"# Test (\d+)(.*?)# Test|\Z", content, re.DOTALL)
    for test_number, test_content in test_sections:
        test = {"test_number": test_number.strip(), "questions": []}
        questions = re.findall(
            r"## Question (\d+):(.*?)## Question|\Z", test_content, re.DOTALL
        )
        for question_number, question_content in questions:
            question = {"question_number": question_number.strip(), "choices": []}
            question_data = re.match(
                r"(.*?)(Explanation.*?)\Z", question_content, re.DOTALL
            )
            if question_data:
                question_text, choices_and_explanation = question_data.groups()
                explanation_matches = re.findall(
                    r"- (\w+)\) (.+?):\n\n>(.*?)\n\n",
                    choices_and_explanation,
                    re.DOTALL,
                )
                for choice, text, explanation in explanation_matches:
                    is_correct = choice.startswith("(")
                    choice = choice.strip("()")
                    user_response = is_correct and question_text.endswith("Incorrect")
                    question["choices"].append(
                        {
                            "choice": choice,
                            "text": text.strip(),
                            "is_correct": is_correct,
                            "user_response": user_response,
                            "explanation": explanation.strip(),
                        }
                    )
                question["question_text"] = question_text.strip()
                question["status"] = (
                    "Incorrect" if question_text.endswith("Incorrect") else "Correct"
                )
                test["questions"].append(question)
        tests.append(test)

    return {"tests": tests}


def save_json(data, json_file):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)


markdown_file = "Review_Guide.md"
json_file = "Review_Guide.json"

data = markdown_to_json(markdown_file)
save_json(data, json_file)
