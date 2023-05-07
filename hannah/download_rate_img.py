import streamlit as st
import pandas as pd
from PIL import Image
import csv
import requests

# Define function to load image from URL
def load_image_from_url(url):
    img = Image.open(requests.get(url, stream=True).raw)
    return img

# Define function to save results to CSV
def save_results_to_csv(results):
    results_df = pd.DataFrame(results, columns=['url', 'rating'])
    results_df.to_csv('results.csv', index=False)

# Define main function
def main(img_urls):
    # Initialize results list
    results = []

    # Loop through each image URL
    for img_url in img_urls:
        # Load image from URL
        img = load_image_from_url(img_url)

        # Display image and rating widget
        st.image(img, caption=img_url, use_column_width=True)
        rating = st.text_input(f'Enter a rating for this image (1-10): {img_url}')
        if rating:
            try:
                rating = int(rating)
                if rating < 1 or rating > 10:
                    raise ValueError
                results.append((img_url, rating))
            except ValueError:
                st.error('Please enter a valid rating (1-10).')
                continue

        # Add a separator between images
        st.markdown('---')

    # Save results to CSV
    save_results_to_csv(results)


with open('results.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    next(reader)
    # Define a list of example image URLs
    img_urls = [row[0] for row in reader]

# Call the main function with the list of image URLs
main(img_urls)
