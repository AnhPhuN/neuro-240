# gets accuracy of predictions
import json

def quantify_accuracy(results):
    correct = 0
    total = 0

    for _, values in results.items():
        correct += sum(values)
        total += len(values)

    if total == 0:
        return 0

    return correct / total

with open('score.json', 'r') as f:
    results = json.load(f)

accuracy = quantify_accuracy(results)
print(f"Accuracy: {accuracy:.2f}")  # Output: Accuracy: 0.56
