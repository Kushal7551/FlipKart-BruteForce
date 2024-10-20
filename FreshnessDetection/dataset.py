import os
import shutil
from sklearn.model_selection import train_test_split

# Directories
output_dir = 'extracted_frames_banana'
label_dir = 'labels'
dataset_dir = 'dataset'

# Create directories for YOLO format
train_images_dir = os.path.join(dataset_dir, 'train', 'images')
train_labels_dir = os.path.join(dataset_dir, 'train', 'labels')
val_images_dir = os.path.join(dataset_dir, 'val', 'images')
val_labels_dir = os.path.join(dataset_dir, 'val', 'labels')

# Create required directories
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get the list of frames and labels
frames = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])
labels = sorted([f for f in os.listdir(label_dir) if f.endswith('.txt')])

# Split into training and validation sets (80% train, 20% validation)
train_frames, val_frames, train_labels, val_labels = train_test_split(frames, labels, test_size=0.2, random_state=42)

# Move the files to train and val folders
for frame, label in zip(train_frames, train_labels):
    shutil.move(os.path.join(output_dir, frame), os.path.join(train_images_dir, frame))
    shutil.move(os.path.join(label_dir, label), os.path.join(train_labels_dir, label))

for frame, label in zip(val_frames, val_labels):
    shutil.move(os.path.join(output_dir, frame), os.path.join(val_images_dir, frame))
    shutil.move(os.path.join(label_dir, label), os.path.join(val_labels_dir, label))

print("Dataset is ready for YOLOv8 training!")
