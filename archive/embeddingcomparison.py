import pytesseract
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define the goal phrase as a sequence of words
goal_phrase = 'finish machine learning project'
goal_seq = goal_phrase.split()

# Load the pre-trained word embedding model
embedding_model = tf.keras.models.load_model('embedding_model.h5')

# Load the screenshot and perform OCR to extract the text
screenshot = cv2.imread('screenshot.png')
text = pytesseract.image_to_string(screenshot)

# Preprocess the text by lowercasing and tokenizing it
text = text.lower()
text_seq = text.split()

# Create a tokenizer to convert the text to sequences of word indices
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text, goal_phrase])
text_seq = tokenizer.texts_to_sequences([text])[0]
goal_seq = tokenizer.texts_to_sequences([goal_phrase])[0]

# Pad the sequences to a fixed length to create a consistent input shape
max_len = max(len(text_seq), len(goal_seq))
text_seq = pad_sequences([text_seq], maxlen=max_len, padding='post')[0]
goal_seq = pad_sequences([goal_seq], maxlen=max_len, padding='post')[0]

# Convert the sequences to embeddings using the pre-trained model
text_emb = embedding_model.predict(np.array([text_seq]))
goal_emb = embedding_model.predict(np.array([goal_seq]))

# Compute the cosine similarity between the embeddings
similarity = np.dot(text_emb, goal_emb.T) / (np.linalg.norm(text_emb) * np.linalg.norm(goal_emb))

# If the similarity is above a certain threshold, classify as on task, otherwise classify as off task
threshold = 0.7
if similarity > threshold:
    print('On task')
else:
    print('Off task')