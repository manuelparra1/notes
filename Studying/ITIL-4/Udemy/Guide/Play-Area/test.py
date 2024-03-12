import re

# Your regex pattern
pattern = r"## Question (?P<question_number>\d+): (?P<correctness>Correct|Incorrect)\n\*\*Which.*\?\*\*\n\n- (?P<correct_answer>[A-D]) .+ \((?P=correctness)\):\n\n> (?P<explanation>.+?)(?=\n\n- [A-D])"

# Your text
text = """
# Test 1

## Question 14: Incorrect

**Which guiding principle is most affected by the customer experience (CX)?**

- A) Progress iteratively with feedback **(Incorrect)**
- B) Focus on value **(Correct)**
- C) Think and work holistically
- D) Start where you are

**Explanation**

- B) Focus on value (Correct):

> This guiding principle emphasizes delivering value to customers and stakeholders. As customer experience (CX) is directly related to the value perceived by the customer, focusing on value is most affected by CX.

- A) Progress iteratively with feedback (Incorrect):

> While this principle involves feedback, it is more about the iterative improvement process rather than directly focusing on customer experience.

- C) Think and work holistically:

> This principle encourages considering the entire system but is not specifically focused on customer experience.

- D) Start where you are:

> This principle emphasizes practicality but doesn't directly address customer experience.

## Question 20: Incorrect

**Which of these are NOT a key focus of the ‘partners and suppliers’ dimension?**

- A) Work-flow management and inventory systems **(Correct)**
- B) Roles and responsibilities
- C) Contracts and agreements
- D) Security and compliance **(Incorrect)**

**Explanation**

- A) Work-flow management and inventory systems (Correct):

> While workflow management and inventory systems are important aspects, they are not key focuses of the 'partners and suppliers' dimension. "Work-flow management and inventory systems" typically falls under the "Service Value System" only supported by the Information Technology Dimension. Partners & Suppliers Dimension is more concerned with roles, responsibilities, contracts, agreements, security, and compliance.

- B) Roles and responsibilities:

> This is a key focus of the 'partners and suppliers' dimension.

- C) Contracts and agreements:

> Also a key focus of the 'partners and suppliers' dimension.

- D) Security and compliance (Incorrect):

> Security and compliance are key focuses of the 'partners and suppliers' dimension.
"""

# Search for matches
matches = re.finditer(pattern, text)

# Loop through matches
for match in matches:
    # Access capture groups by name using groupdict()
    match_dict = match.groupdict()
    print("Question Number:", match_dict["question_number"])
    print("Correctness:", match_dict["correctness"])
    print("Correct Answer:", match_dict["correct_answer"])
    print("Explanation:", match_dict["explanation"])
    print()  # Print an empty line for readability
