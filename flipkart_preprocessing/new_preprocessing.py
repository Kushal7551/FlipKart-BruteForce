import cv2
import numpy as np

def preprocess_image_for_ocr(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Step 1: Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Step 2: CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  # Reduced clipLimit for more natural contrast
    l = clahe.apply(l)

    # Merge channels back into LAB image and convert back to BGR
    enhanced_lab = cv2.merge((l, a, b))
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    # Step 3: Denoising
    denoised = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 15, 15, 7, 21)

    # Step 4: Sharpening with a different kernel for fine-tuning
    kernel_sharpening = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])  # Lighter sharpening filter
    sharpened = cv2.filter2D(denoised, -1, kernel_sharpening)

    # Step 5: Binarization using Otsu's thresholding
    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the processed image
    cv2.imwrite(output_path, binary_image)

# Example usage
image_path = "trial.jpeg"  # Input image path
output_path = "output_processed.jpg"  # Output path for the processed image
preprocess_image_for_ocr(image_path, output_path)
