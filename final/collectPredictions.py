# cleaned data to predictions

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
You are taskGPT, an AI that takes in data taken from a computer screen and describes what is happening on the screen. The format you take in is:
[x1,y1,x2,y2] “content info”
Where x1,y1,x2,y2 are integers that represent the bounding box pixel position of the text on the screen, counting from the top left with dimensions 3024 × 1964, and “content info” is the text contained inside the box. Your job is to understand the relationships between these bounding boxes intelligently based on their locations, to figure out groupings like a tweet with an image and caption, etc. You are given a series of questions to answer. 
Below is the content on the screen:
"""
suffix = "Answer in the following format separating answers with ###: \"\"\"answer 1 ### answer 2...\"\"\""

# load json labels
with open('data/labels/qa_labels.json', 'r') as f:
    qa_labels = json.load(f)

with open('data/labels/predictions.json') as f:
    predictions = json.load(f)

if __name__ == "__main__":
    for i in range(0, 26):
        print("Doing: ", i)
        with open("data/labelsformatted/"+str(i)+".txt", "r") as f:
            screen_data = f.read()
        questions = [d["Question"] for d in qa_labels[str(i)]]
        user_prompts = "\n".join(["- " + item for item in questions])
        response = getCompletion(screen_data, user_prompts)
        print("RESPONSE: ", response)
        responses = my_array = response.split("###")
        print("responses", responses)
        predictions[str(i)].append(responses)


    # Write the updated data back to the JSON file 
    with open("data/labels/predictions-3.5.json", "w") as f:
        json.dump(predictions, f)
