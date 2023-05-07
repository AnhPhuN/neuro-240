# gets accuracy of predictions
import json

def quantify_accuracy(results):
    correct = 0
    total = 0

    for _, values in results.items():
        filtered_values = [x for x in values if x != 2] # 2 means inconclusive answer
        correct += sum(filtered_values)
        total += len(filtered_values)
    print("correct: ", correct, "total: ", total)
    if total == 0:
        return 0

    return correct / total

# def verify_prediction_lengths(filename, qa_labels_file):


if __name__ == "__main__":
    with open('data/labels/score-4-2.json', 'r') as f:
        results = json.load(f)

    accuracy = quantify_accuracy(results)
    print(f"Accuracy: {accuracy:.2f}")  # Output: Accuracy: 0.56
