# compare prediction and ground truth


import openai
import os
import json

def getCompletion(screen_content, user_prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
    #   model="gpt-4",
      messages=[
            {"role": "system", "content": start_prompt},
            {"role": "user", "content": screen_content + "\n\n" + user_prompt + "\n\n" + suffix}
        ]
    )
    return response['choices'][0]['message']['content']

start_prompt = """
You are QuantifierGPT, an AI that takes in an AI model's predicted answer to a 
question about what is going on on a computer screen, as well as the ground truth answer to the question.
"""
# suffix = "Answer in the following format separating answers with ###: \"\"\"answer 1 ### answer 2...\"\"\""

# load json labels
with open('data/labels/qa_labels.json', 'r') as f:
    qa_labels = json.load(f)

with open('data/labels/predictions.json') as f:
    predictions = json.load(f)

for i in range(1, 2):
    with open("data/labelsformatted/"+str(i)+".txt", "r") as f:
        screen_data = f.read()
    questions = [d["Question"] for d in qa_labels[str(i)]]
    ground_truths = [d["Answer"] for d in qa_labels[str(i)]]
    if questions != ground_truths:
        print("Error: Questions list is not equal to Ground Truths list.")
        exit() 
    user_prompts = "\n".join(["- " + item for item in questions])
    # response = getCompletion(screen_data, user_prompts)
    # print("RESPONSE: ", response)
    # responses = my_array = response.split("###")
    # print("responses", responses)
    # predictions[str(i)].append(responses)


# Write the updated data back to the JSON file 
with open("data/labels/predictions.json", "w") as f:
    json.dump(predictions, f)
