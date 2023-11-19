import os
import cv2

# Set the path for the Images folder
path = "F:\ADDANISH\coding\pythonprojects\c117\Images"

# Create a list variable named Images
images = []

# Check each file in the folder
for file in os.listdir(path):
    # Separate the name and extension from the file name
    name, extension = os.path.splitext(file)
    
    # Check if the extension matches the image extension
    if extension in ['.jpg', '.jpeg', '.png']:
        # Create the full file path
        file_name = os.path.join(path, file)
        
        # Add the file to the images list
        images.append(file_name)

# Get the number of images
count = len(images)

# Read the first image to get width, height, and channels
frame = cv2.imread(images[0])
height, width, channels = frame.shape

# Create a tuple variable size
size = (width, height)

# Print size to check the result
print(size)

# Create a video writer
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to the video writer
for i in range(count):
    # Read each image
    img = cv2.imread(images[i])
    
    # Add the image to the video
    out.write(img)

# Release the video writer
out.release()

# Print a message when the video is complete
print("Done")
