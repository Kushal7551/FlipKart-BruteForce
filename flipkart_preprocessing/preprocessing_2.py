import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display and save the image
def display_and_save(image, step_name):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide the axes
    plt.show()
    cv2.imwrite(f"{step_name}.jpg", image)  # Save image with step name

# 1. Inverted Image
def invert_image(image):
    return cv2.bitwise_not(image)

# 2. Rescaling Image
def rescale_image(image, scale_percent=150):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# 3. Binarization
def binarize_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return binary_image

# 4. Noise Removal
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

# 5. Dilation and Erosion
def dilate_and_erode(image, kernel_size=2, iterations=1):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=iterations)
    return eroded_image

# 6. Deskewing Image (Finding Skew Angle)
def get_skew_angle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    contours, _ = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    largest_contour = contours[0]
    min_area_rect = cv2.minAreaRect(largest_contour)
    angle = min_area_rect[-1]

    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

# Rotate Image Based on Skew Angle
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

# 7. Remove Borders
def remove_borders(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    x, y, w, h = cv2.boundingRect(contours[0])
    cropped = image[y:y+h, x:x+w]
    return cropped

# 8. Add Missing Borders
def add_missing_borders(image, border_size=10):
    return cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])

# 9. Handle Transparency / Alpha Channel (Convert to RGB)
def remove_alpha_channel(image):
    if len(image.shape) == 3 and image.shape[2] == 4:  # Check if the image has an alpha channel
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return image

# Main Function to Preprocess the Image
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Step 9: Remove alpha channel if present
    img = remove_alpha_channel(img)
    display_and_save(img, "step_1_original")

    # Step 1: Inverted Image
    img_inverted = invert_image(img)
    display_and_save(img_inverted, "step_2_inverted")

    # Step 2: Rescaling the image
    img_rescaled = rescale_image(img_inverted, scale_percent=150)
    display_and_save(img_rescaled, "step_3_rescaled")

    # Step 3: Binarization
    img_binarized = binarize_image(img_rescaled)
    display_and_save(img_binarized, "step_4_binarized")

    # Step 4: Noise Removal
    img_no_noise = noise_removal(img_binarized)
    display_and_save(img_no_noise, "step_5_noise_removed")

    # Step 5: Dilation and Erosion
    img_dilated_eroded = dilate_and_erode(img_no_noise)
    display_and_save(img_dilated_eroded, "step_6_dilated_eroded")

    # Step 6: Deskewing the image
    # skew_angle = get_skew_angle(img)
    # img_deskewed = rotate_image(img, skew_angle)
    # display_and_save(img_deskewed, "step_7_deskewed")

    # Step 7: Removing Borders
    img_no_borders = remove_borders(img_dilated_eroded)
    display_and_save(img_no_borders, "step_8_borders_removed")

    # Step 8: Adding Missing Borders
    img_with_borders = add_missing_borders(img_no_borders)
    display_and_save(img_with_borders, "step_9_with_borders")


# Example usage
image_path = "trial.jpeg"  # Ensure this path is correct
preprocess_image(image_path)
