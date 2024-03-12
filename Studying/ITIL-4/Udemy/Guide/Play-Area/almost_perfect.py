import re
import json

def parse_markdown_file(filename):
    questions = []
    with open(filename, 'r') as file:
        content = file.read()
        question_blocks = content.split("## ")[1:]  # Split content into question blocks

        for block in question_blocks:
            question = {}
            lines = block.split("\n")

            # Extract question number and status, with error handling
            question_number_status_match = re.match(r'Question (\d+): (Incorrect)', lines[0])
            if not question_number_status_match:
                print(f"Skipping block as it does not match expected pattern: {lines[0]}")
                continue
            question_number, status = question_number_status_match.groups()
            question['question_number'] = int(question_number)
            question['status'] = status

            # Extract question text
            question_text = lines[2].strip()
            question['question'] = question_text

            # Extract choices and determine correct, incorrect choices, and user response
            choices = []
            for line in lines[3:]:
                if "- " in line:
                    choice_match = re.search(r'- ([A-D])\) ([^\(]+) \((Correct|Incorrect)\)', line)
                    if choice_match:
                        letter, choice_text, correctness = choice_match.groups()
                        choice = {
                            'letter': letter,
                            'text': choice_text.strip(),
                            'is_correct': correctness == "Correct",
                            'user_response': correctness == "Incorrect"
                        }
                        choices.append(choice)
            question['choices'] = choices

            # Add question to list of questions
            questions.append(question)

    return questions

# Parse the markdown file
parsed_questions = parse_markdown_file("Review_Guide.md")

# Write the parsed questions to a JSON file
with open('Review_Guide.json', 'w') as json_file:
    json.dump(parsed_questions, json_file, indent=2)

print("Conversion completed successfully!")
