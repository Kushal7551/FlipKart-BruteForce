import os
import cv2
import csv

# Directory paths
output_dir = 'extracted_frames_banana'
label_dir = 'labels'  # Create a folder to save label txt files
csv_file = 'frame_score_mapping.csv'  # Path to the CSV file

if not os.path.exists(label_dir):
    os.makedirs(label_dir)

# Load freshness scores from the CSV
def load_freshness_scores(csv_file):
    frame_score_mapping = {}
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            frame_score_mapping[row['frame']] = float(row['score'])
    return frame_score_mapping

# Load the frame scores from the CSV
frame_score_mapping = load_freshness_scores(csv_file)

# Iterate over the frames and create corresponding label files
for frame in sorted(os.listdir(output_dir)):
    if frame.endswith('.png'):
        # Load the image to get dimensions
        img_path = os.path.join(output_dir, frame)
        img = cv2.imread(img_path)
        height, width, _ = img.shape

        # Get the corresponding freshness score from the CSV
        freshness_score = frame_score_mapping.get(frame, 0)  # Default to 0 if not found

        # For now, we use the entire image as the bounding box
        # Adjust this part if you have actual bounding box coordinates
        x_center = 0.5  # Center of the image
        y_center = 0.5
        box_width = 0.7  # Assume a box that covers 70% of width
        box_height = 0.55  # Assume a box that covers 55% of height

        # Normalize freshness score between 0 and 1 for YOLO format
        normalized_freshness_score = freshness_score / 100.0

        # YOLO format: <class> <x_center> <y_center> <width> <height> <freshness_score>
        label_file = os.path.join(label_dir, f"{frame.split('.')[0]}.txt")
        with open(label_file, 'w') as f:
            f.write(f"0 {x_center} {y_center} {box_width} {box_height} \n")
