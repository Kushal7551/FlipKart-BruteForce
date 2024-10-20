import os
import cv2
import numpy as np

# Set your video file path, timestamps, and output directory
video_file = 'banana.mp4'  # Replace with your video file path
start_time = '00:00:08'  # Start timestamp (in format HH:MM:SS)
end_time = '00:00:30'  # End timestamp (in format HH:MM:SS)
output_dir = 'extracted_frames_banana'
fps = 30  # Frames per second

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Extract frames using ffmpeg from start_time to end_time
os.system(f"ffmpeg -i {video_file} -ss {start_time} -to {end_time} -vf fps={fps} {output_dir}/frame_%04d.png")

# Get list of all frames
frames = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])

# Number of frames
num_frames = len(frames)

# Assign a freshness score from 1 to 100 linearly across all frames
scores = np.linspace(1, 100, num_frames)

# Save the frames with their assigned scores
frame_score_mapping = {}
for i, frame in enumerate(frames):
    # Read the image (for example, for further processing)
    img_path = os.path.join(output_dir, frame)
    img = cv2.imread(img_path)
    
    # Assign freshness score
    score = scores[i]
    
    # Save the score in the dictionary
    frame_score_mapping[frame] = score
    
    # (Optional) If you want to overlay the score on the image:
    cv2.putText(img, f"Freshness Score: {int(score)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Save the image with score overlay (optional)
    cv2.imwrite(os.path.join(output_dir, f"scored_{frame}"), img)

# Print the mapping of frames to their scores (or save it as a CSV)
print(frame_score_mapping)

# (Optional) Save the frame-score mapping as a CSV
import csv
with open('frame_score_mapping.csv', 'w', newline='') as csvfile:
    fieldnames = ['frame', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for frame, score in frame_score_mapping.items():
        writer.writerow({'frame': frame, 'score': score})
