
import pickle
import json
import numpy as np


with open('att_dict_simplified.p', 'rb') as f:
    att_dict = pickle.load(f)

print(att_dict)

# Convert the data to a JSON string
json_str = json.dumps(att_dict)

# Save the JSON string to a text file
with open('data.txt', 'w') as f:
    f.write(json_str)
    