import cv2
import os

# Path to the directory containing your images
image_folder = "F:\1aa\coding\python projects\c117\Images"

# List the image files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

# Sort the images based on their names
images.sort()

# Set video properties
frame_width, frame_height = 640, 480
video_name = 'friendship_day_video.avi'  # Output video file name
fps = 1  # Frames per second

# Create a video writer object
video_writer = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

# Iterate through the images and add them to the video
for image in images:
    image_path = os.path.join(image_folder, image)
    img = cv2.imread(image_path)
    img = cv2.resize(img, (frame_width, frame_height))  # Resize image to fit video frame
    video_writer.write(img)

# Release the video writer object
video_writer.release()
