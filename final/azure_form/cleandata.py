import json


def SimpleBBOX(values):
    return values[:2] + values[4:6]

def format_result(json_obj):
    formatted_word = []
    formatted_paragraph = []
    for paragraph in json_obj["analyzeResult"]["paragraphs"]:
        x1, y1, x2, y2 = SimpleBBOX(paragraph["boundingRegions"][0]["polygon"])
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

for i in range(16):
    cleanData(str(i) + ".json")