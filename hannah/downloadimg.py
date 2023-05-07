import csv
import os
import requests
from PIL import Image


# Open the CSV file
with open('results.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    next(reader)
    # Define a list of example image URLs
    img_urls = [row[0] for row in reader]

print('hee', img_urls)
# Loop through each row of the CSV file
for img_url in img_urls:
    print("hello", img_url)

    # Download the image from the URL
    response = requests.get(img_url)

    # Save the image to the downloaded_images directory
    with open(f'downloaded_images/{img_url.split("/")[-1]}', 'wb') as f:
        f.write(response.content)

    # Optional: Display the downloaded image
    img = Image.open(f'downloaded_images/{img_url.split("/")[-1]}')
    img.show()
