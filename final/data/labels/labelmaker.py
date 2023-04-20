# makes json label structure

import json

n = 90  # number of sections

data = {}
for i in range(1, n+1):
    section = []
    for j in range(4):
        question = " "
        answer = " "
        section.append({"Question": question, "Answer": answer})
    data[str(i)] = section

with open("qa_labels.json", "w") as file:
    json.dump(data, file, indent=2)

print(json.dumps(data, indent=2))
