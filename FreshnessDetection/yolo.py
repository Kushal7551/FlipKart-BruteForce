import cv2

def draw_yolo_box(image_path, yolo_box, label="banana", freshness_score=None):
    # Load the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Extract YOLO format values (assumed values are normalized)
    class_id, x_center, y_center, box_width, box_height = yolo_box

    # Convert YOLO normalized values to absolute pixel values
    x_center_abs = int(x_center * width)
    y_center_abs = int(y_center * height)
    box_width_abs = int(box_width * width)
    box_height_abs = int(box_height * height)

    # Calculate top-left and bottom-right corners of the bounding box
    x1 = int(x_center_abs - (box_width_abs / 2))
    y1 = int(y_center_abs - (box_height_abs / 2))
    x2 = int(x_center_abs + (box_width_abs / 2))
    y2 = int(y_center_abs + (box_height_abs / 2))

    # Draw the rectangle (bounding box)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Add label and freshness score, if provided
    label_text = f"{label}"
    if freshness_score is not None:
        label_text += f" (Freshness: {freshness_score})"
    
    # Put text on the image
    cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Save or display the result
    cv2.imwrite('image_with_yolo_box.png', image)
    cv2.imshow('Image with YOLO Bounding Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Image path
image_path = 'extracted_frames_banana/frame_0647.png'

# YOLO format bounding box: [class_id, x_center, y_center, width, height] - all values normalized
yolo_box = [0, 0.5, 0.5, 0.7, 0.55]  # Example normalized values
freshness_score = 85  # Example freshness score

# Draw the YOLO bounding box
draw_yolo_box(image_path, yolo_box, label="banana", freshness_score=freshness_score)
