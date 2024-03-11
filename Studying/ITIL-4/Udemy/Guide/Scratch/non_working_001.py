import json
import re


def markdown_to_json(markdown_file):
    with open(markdown_file, "r") as file:
        markdown_text = file.read()

    tests = []
    test_sections = re.split(r"(?m)^## ", markdown_text)[1:]

    for test_section in test_sections:
        test_info, *question_sections = test_section.split("## ")
        test_number = re.search(r"Test (\d+)", test_info).group(1)
        questions = []

        for question_section in question_sections:
            question_info, *choices_sections = question_section.split("**Explanation**")
            question_number, status = re.search(
                r"Question (\d+): (\w+)", question_info
            ).groups()
            question_text = question_info.split(":")[-1].strip()

            choices = []
            for choice_section in choices_sections:
                choice_match = re.search(r"- (\w+)\) (.+?)\n>\s*(.+)", choice_section)
                if choice_match:
                    choice, text, explanation = choice_match.groups()
                    is_correct = choice == re.search(r"\((\w+)\)", explanation).group(1)
                    choices.append(
                        {
                            "choice": choice,
                            "text": text.strip(),
                            "is_correct": is_correct,
                            "user_response": False,
                            "explanation": explanation.strip(),
                        }
                    )

            questions.append(
                {
                    "question_number": question_number,
                    "status": status,
                    "question_text": question_text.strip(),
                    "choices": choices,
                }
            )

        tests.append({"test_number": test_number, "questions": questions})

    return {"tests": tests}


markdown_file = "Review_Guide.md"
json_data = markdown_to_json(markdown_file)

# Write JSON data to a file
output_file = "Review_Guide.json"
with open(output_file, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON data has been saved to {output_file}")
