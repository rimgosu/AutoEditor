from PIL import Image
from PIL import ImageGrab
import numpy as np
from sklearn.cluster import KMeans

def get_dominant_color_from_file(image_file_path, n_colors=1):
    # Open the image file
    image = Image.open(image_file_path)

    # Convert the image to a numpy array
    image_np = np.array(image)

    # Reshape the numpy array to be a list of pixels
    pixel_list = image_np.reshape(-1, 3)

    # Use KMeans to cluster the pixels into n_colors groups
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(pixel_list)

    # Get the RGB values of the centroid of each group
    dominant_colors = kmeans.cluster_centers_.astype(int)
    print(dominant_colors)

    # Return the most dominant color as a tuple of RGB values
    return tuple(dominant_colors[np.argmax(kmeans.labels_)])

get_dominant_color_from_file(r"C:\Users\rimgosu\Desktop\ShareFolder\git\AutoEditor\이미지 595.png")

