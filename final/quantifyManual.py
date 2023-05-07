import json

# Read qa_labels.json
with open('data/labels/qa_labels.json', 'r') as f:
    qa_labels = json.load(f)

# Read predictions.json
with open('data/labels/predictions-4-2.json', 'r') as f:
    predictions = json.load(f)

score_path = 'data/labels/score-4-2.json'

# Initialize score dictionary
with open(score_path, 'r') as f:
    score = json.load(f)

# Iterate through the dictionaries
for index in qa_labels:
    qa_list = qa_labels[index]
    pred_list = predictions[index][0]
    print("------------------------------------------------------")
    # Print questions from qa_labels and predictions
    for i, qa in enumerate(qa_list):
        print(f"Index: {index}, Question: {qa['Question']}")
        print(f"Label: {qa['Answer']}")
        print(f"Prediction: {pred_list[i]}\n")

    # Collect user input and store in score dictionary
    user_input = input(f"Enter the scores for index {index} separated by comma (e.g. 1,0,1): ")
        
    score[index] = [int(x) for x in user_input.split(',')]
    with open(score_path, 'w') as f:
        json.dump(score, f)
# Write scores to score.json


