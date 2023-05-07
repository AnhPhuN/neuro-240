# compare prediction and ground truth


import openai
import os
import json

def getCompletion(user_prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
      model="gpt-4",
    #   model="gpt-4",
      messages=[
            {"role": "system", "content": start_prompt},
            {"role": "user", "content": user_prompt + "\n\n" + suffix}
        ]
    )
    return response['choices'][0]['message']['content']

start_prompt = """
You are QuantifierGPT, an AI that takes in an AI model's predicted answer to a 
question about what is going on on a computer screen, as well as the ground truth answer to the question.
"""
suffix = "Your job is to check each Question, Label, and Prediction pair, and return 1 if the prediction was correct, or 0 if it was wrong. Since you have multiple things to classify, return your answer as simply 0s and 1s separated by commas. For example, '0,1,1' means question 1 was predicted wrong, and question 2 and 3 were correct."

# Read qa_labels.json
with open('data/labels/qa_labels.json', 'r') as f:
    qa_labels = json.load(f)

# Read predictions.json
with open('data/labels/predictions-4-2.json', 'r') as f:
    predictions = json.load(f)

score_path = 'data/labels/score-4-2-auto.json'

# Initialize score dictionary
with open(score_path, 'r') as f:
    score = json.load(f)

# Iterate through the dictionaries
for index in qa_labels:
    user_prompt = ""
    if int(index) == 7:
        continue
    qa_list = qa_labels[index]
    pred_list = predictions[index][0]
    print("------------------------------------------------------")
    # Print questions from qa_labels and predictions
    for i, qa in enumerate(qa_list):
        print(f"Index: {index}, Question: {qa['Question']}")
        print(f"Label: {qa['Answer']}")
        print(f"Prediction: {pred_list[i]}\n")
        user_prompt += "Question: " + qa['Question'] + "\nLabel: " + qa['Answer'] + "\nPrediction: " + pred_list[i]


    # Collect user input and store in score dictionary
    response = getCompletion(user_prompt)
    print("response: ", response)
        
    score[index] = [int(x) for x in response.split(',')]
    with open(score_path, 'w') as f:
        json.dump(score, f)
    user_input = input("Press enter to move to the next index.")
# Write scores to score.json