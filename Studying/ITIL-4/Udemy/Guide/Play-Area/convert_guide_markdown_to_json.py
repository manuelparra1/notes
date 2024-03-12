import json
import re


def parse_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    questions_list = []
    question_blocks = re.split(r"\n(?=## Question \d+: Incorrect)", content)[
        1:
    ]  # Split the document by questions

    for block in question_blocks:
        # Extracting question number and text
        question_header = re.search(
            r"## Question (\d+): Incorrect\s*\n+(.*?)\n", block, re.DOTALL
        )
        if not question_header:
            continue
        question_number, question_text = question_header.groups()
        question_text = question_text.strip()

        # Extracting choices and explanations from the Explanation section
        choice_explanations = re.findall(
            r"- ([A-D])\) (.*?):\s*\n(?:> (.*?))?(?=\n- [A-D]|\n##|$)", block, re.DOTALL
        )

        choices_data = [
            {
                "letter": choice[0],
                "text": choice[1]
                .strip()
                .replace(":", "")
                .replace("**(Correct)**", "")
                .replace("**(Incorrect)**", ""),
                "is_correct": "**(Correct)**" in choice[1],
                "user_response": "**(Incorrect)**" in choice[1],
                "explanation": (choice[2] or "").strip(),
            }
            for choice in choice_explanations
        ]

        # Constructing the question dictionary
        question_dict = {
            "question_number": question_number,
            "question_text": question_text,
            "choices": choices_data,
            "status": "Incorrect",
        }

        questions_list.append(question_dict)

    return questions_list


def save_to_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Adjust the path as necessary
questions_data = parse_markdown_file("Review_Guide.md")
save_to_json(questions_data, "Review_Guide.json")

print("Conversion to JSON completed.")
