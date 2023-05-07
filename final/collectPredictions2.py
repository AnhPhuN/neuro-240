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
            {"role": "user", "content": screen_content + "\n\n" + user_prompt}
        ]
    )
    return response['choices'][0]['message']['content']

start_prompt = """
You take in data taken from a computer screen and determines if someone is actually focused on a predefined task they gave. The format you take in is:
[x1,y1,x2,y2] “content info”
Where x1,y1,x2,y2 are integers that represent the bounding box pixel position of the text on the screen, counting from the top left with dimensions 3024 x 1964, and “content info” is the text contained inside the box.
Below is the content on the screen:
"""
suffix = "Answer the above questions in the following format separating each answer with ###: \"\"\"'answer 1' ### 'answer 2'...\"\"\""

# load json labels
with open('data/labels/qa_labels.json', 'r') as f:
    qa_labels = json.load(f)

prediction_path = 'data/labels/predictions-3.5-2.json'

with open(prediction_path) as f:
    predictions = json.load(f)

if __name__ == "__main__":
    for i in range(6, 7):
        print("Doing: ", i)
        with open("data/labelsformatted/"+str(i)+".txt", "r") as f:
            screen_data = f.read()
        questions = [d["Question"] for d in qa_labels[str(i)]]
        user_prompts = "\n".join(["- " + item for item in questions])
        print(user_prompts)
        response = getCompletion(screen_data, user_prompts + "\n\n" + suffix)
        print("RESPONSE: ", response)
        responses = my_array = response.split("###")
        print("responses", responses)
        predictions[str(i)].append(responses)


    # Write the updated data back to the JSON file 
    with open(prediction_path, "w") as f:
        json.dump(predictions, f)
