import re
import json

def parse_markdown(md_path):
    question_pattern = re.compile(r"## Question (\d+): (Incorrect)")
    # Here regex is adjusted to ensure it matches until the next "## Question" or end of file to properly split questions
    choice_pattern = re.compile(r"- ([A-D])\) ([^\n]+)")
    explanation_pattern = re.compile(r"- ([A-D])\) (.+?):\n\n> (.+?)(?=(\n\n- [A-D])|\Z)", re.S)
    
    questions = []

    with open(md_path, 'r', encoding='utf-8') as md_file:
        content = md_file.read()

    # Find all questions instead of splitting to avoid IndexError
    question_matches = question_pattern.finditer(content)
    # Collect start positions of all questions to slice content correctly
    question_positions = [(m.start(), m.group(1), m.group(2)) for m in question_matches]

    for i, (start_pos, question_num, status) in enumerate(question_positions):
        # Determine end of current question content by next question start or end of content
        end_pos = question_positions[i + 1][0] if i + 1 < len(question_positions) else None
        question_content = content[start_pos:end_pos]

        # Search for the question text within the extracted content
        question_text_match = re.search(r"\*\*(.+?)\*\*", question_content)
        
        if not question_text_match:
            print(f"Could not find question text for question number: {question_num}")
            continue

        question_text = question_text_match.group(1)
        
        choices = []
        for c in choice_pattern.findall(question_content):
            is_correct = "(Correct)" in c[1]
            user_response = "(Incorrect)" in c[1]
            choice_text = re.sub(r" \((Correct|Incorrect)\)", "", c[1])
            choices.append({
                "letter": c[0],
                "text": choice_text,
                "is_correct": is_correct,
                "user_response": user_response,
                "explanation": "",
            })

        explanations = explanation_pattern.findall(question_content)
        for explanation in explanations:
            for choice in choices:
                if choice['letter'] == explanation[0]:
                    choice['explanation'] = explanation[2]

        questions.append({
            "number": question_num,
            "status": status,
            "question_text": question_text,
            "choices": choices,
        })

    return questions

def save_json(questions, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(questions, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    md_path = 'Review_Guide.md'
    json_path = 'Review_Guide.json'
    questions = parse_markdown(md_path)
    save_json(questions, json_path)
    print("Review guide converted to JSON successfully.")
