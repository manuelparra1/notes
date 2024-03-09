import re
import sys


def bold_characters(text):
    # Function to apply markdown to the word based on bold count
    def apply_markdown(word, bold_count):
        if bold_count == 1:
            return f"**{word[:1]}**{word[1:]}"
        elif bold_count == 2:
            return f"**{word[:2]}**{word[2:]}"
        elif bold_count == 3:
            return f"**{word[:3]}**{word[3:]}"
        elif bold_count >= 4:
            return f"**{word[:4]}**{word[4:]}"

    # Function to count vowels in a word
    def count_vowels(word):
        vowels = "aeiouy"
        return sum(1 for char in word if char.lower() in vowels)

    # Regular expression to match markdown formatting
    markdown_regex = re.compile(r"(\*\*.+?\*\*)")

    # Process each line in the text
    lines = text.split("\n")
    formatted_lines = []
    for line in lines:
        # Find markdown formatting in the line
        matches = markdown_regex.findall(line)
        if matches:
            # Process each match in the line
            for match in matches:
                # Replace markdown formatting with processed text
                processed_match = apply_markdown(
                    match, min(4, len(re.findall(r"\b\w+\b", match)))
                )
                line = line.replace(match, processed_match)

        formatted_lines.append(line)

    return "\n".join(formatted_lines)


# Function to read input file
def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    # Check if input file is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.md")
        sys.exit(1)

    input_file = sys.argv[1]
    text = read_file(input_file)
    formatted_text = bold_characters(text)

    # Write to output.md
    with open("output.md", "w") as file:
        file.write(formatted_text)
