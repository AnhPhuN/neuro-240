# json to cleaned data

import json


def SimpleBBOX(coordinates):
    x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[2][0], coordinates[2][1]
    return int(x1//10*10), int(y1//10*10), int(x2//10*10), int(y2//10*10)

def format_result(json_obj):
    formatted_word = []
    formatted_paragraph = []
    for paragraph in json_obj["paragraphs"]:
        x1, y1, x2, y2 = SimpleBBOX(paragraph["bounding_regions"][0]["polygon"])
        formatted_paragraph.append(f"[{x1},{y1},{x2},{y2}] \"{paragraph['content']}\"")
    return formatted_word, formatted_paragraph

def cleanData(filename):
    with open("data/rawLabels/" + filename, "r") as f:
        json_obj = json.load(f)

    formatted_word, formatted_paragraph = format_result(json_obj)
    txtfilename = filename.replace(".json", ".txt")
    with open("data/labelsformatted/" + txtfilename, "w") as file:
        for element in formatted_paragraph:
            file.write(str(element) + "\n")

for i in range(16, 40):
    print("doing num: ", i)
    cleanData(str(i) + ".json")