import re
import json

def parse_markdown_file(filename):
    # Function to extract and sort choices based on the letter
    def sort_choices(choice):
        return choice['letter']

    questions = []
    with open(filename, 'r') as file:
        content = file.read()
        # Splitting questions more reliably
        question_blocks = re.split(r'\n## Question ', content)

        for block in question_blocks[1:]:  # Start from the first question (skip any header content)
            question = {}
            block = "## Question " + block  # Add back the identifier removed by split
            
            # Using more generalized regex patterns for robust parsing
            question_number_match = re.search(r'## Question (\d+): (Incorrect)', block)

            # Skip if the question number and status pattern is not found
            if not question_number_match:
                continue

            question_number, status = question_number_match.groups()
            question['question_number'] = int(question_number)
            question['status'] = status

            # Extract question text
            question_text_match = re.search(r'\*\*(.*?)\*\*', block, re.DOTALL)
            if question_text_match:
                question['question'] = question_text_match.group(1).strip()

            # Initialize choices list; capture and sort choices across the broader content
            choices = []
            for letter in ['A', 'B', 'C', 'D']:
                choice_pattern = rf"\n- {letter}\) (.*?)\n"
                choice_match = re.search(choice_pattern, block, re.DOTALL)
                correct_choice_match = re.search(rf"(?:Explanation.+?\n{letter}\): (Correct)|\({letter}\) (?:.+?) \(Correct\))", block, re.DOTALL)

                if choice_match:
                    choice_text = choice_match.group(1).strip()
                    is_correct = bool(correct_choice_match)
                    choices.append({
                        'letter': letter,
                        'text': choice_text,
                        'is_correct': is_correct,
                        'user_response': not is_correct and status == "Incorrect"  # Assume false unless proven otherwise
                    })

            choices.sort(key=sort_choices)
            question['choices'] = choices

            questions.append(question)

    return questions

# Parse the markdown file and handle exceptions if file is not found or any other IO error occurs
try:
    parsed_questions = parse_markdown_file("Review_Guide.md")
    # Write the parsed questions to a JSON file
    with open('Review_Guide.json', 'w') as json_file:
        json.dump(parsed_questions, json_file, indent=2)
    print("Conversion completed successfully!")
except IOError as e:
    print(f"An error occurred: {e.strerror}")
