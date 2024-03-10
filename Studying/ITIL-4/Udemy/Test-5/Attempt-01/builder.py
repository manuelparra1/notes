import re

with open("Test_5.md", encoding="utf-8") as f:
    text = f.read()

explanations = re.findall(r"\*\*Explanation\*\*\n<br>\n(.*?)\n## ", text, re.DOTALL)

for i, exp in enumerate(explanations):
    print(f"**Question {i+1} Explanation:**")
    print("<br>")
    print(exp)
