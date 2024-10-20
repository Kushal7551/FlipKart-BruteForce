# Smart Vision :  Grid  Submission

This repository contains our solutions for the Flipkart Grid Challenge, addressing a range of computer vision tasks including Optical Character Recognition (OCR), image recognition, and the freshness detection of produce.

## Format Overview


| **Percentage** | **Task**                                    | **Details**                                                                 |
|----------------|---------------------------------------------|-----------------------------------------------------------------------------|
| **20%**        | **OCR to Extract Details from Images/Labels**| Extract details such as brand name, pack size, and other information from packaging materials using OCR. |
| **10%**        | **Using OCR to Get Expiry Date Details**     | Utilize OCR to read expiry dates and MRP details printed on items for validation purposes. |
| **30%**        | **Image Recognition and IR Based Counting**  | Implement machine learning to recognize brands, count items, and extract other details from images. |
| **40%**        | **Detecting Freshness of Fresh Produce**     | Predict the shelf life of fresh fruits and vegetables by assessing their freshness through visual cues and patterns. |

---

## Solution:

## Task 1 & 2
### Preprocessing Techniques for Image enhancement:
 The preprocessing pipeline uses multiple image processing techniques to improve image quality and structure, making it more suitable for OCR tasks. The steps include denoising, sharpening, scaling, binarization, border handling, and more.

Method 1:
1. *Image Loading*: Loads the image from the given path.
2. *LAB Color Space Conversion*: Converts the image from the BGR color space to LAB, which separates the lightness (L) channel from the color (A and B) channels.
3. *Contrast Limited Adaptive Histogram Equalization (CLAHE)*: Enhances the contrast of the image using CLAHE, applied only to the L channel (lightness) of the LAB image. CLAHE prevents over-amplifying noise while improving contrast in local regions of the image.
4. *LAB to BGR Conversion*: Converts the LAB image back to BGR format after contrast enhancement.
5. *Denoising*: Reduces noise using the Non-Local Means Denoising algorithm for colored images, preserving details while smoothing unwanted noise.
6. *Image Sharpening*: A kernel-based sharpening filter is applied to enhance text and other important details in the image.
7. *Saving the Preprocessed Image*: The final preprocessed image is saved to the specified output path.

Method 2:
1. *Image Loading and Alpha Channel Removal*: The image is loaded, and if it contains an alpha channel, it's converted to a standard RGB image.
2. *Color Inversion*: The image colors are inverted using a bitwise NOT operation.
3. *Rescaling*: The image is resized by 150% to improve OCR accuracy.
4. *Binarization*: The image is converted to grayscale and then binarized using Otsu’s thresholding.
5. *Noise Removal*: Morphological transformations (dilation and erosion) are applied to remove noise.
6. *Dilation and Erosion*: These operations are used to enhance text features.
7. *Border Removal*: Borders around the document or text are removed using contour detection.
8. *Border Addition*: Additional borders are added to ensure no text is cropped.
9. (Optional) *Deskewing*: Skew angle detection and correction to straighten tilted images.





# OCR-based Content Extraction using PaddleOCR and Gemini API

This project uses **PaddleOCR** to extract text from images and the **Gemini API** to process and display specific content such as brand names, expiry dates, and other key details. 

### Key Features:
- **Text detection and recognition** via PaddleOCR.
- **Content extraction** (e.g., brand names, expiry dates) using the Gemini API.
- Clean and structured output display.

### Requirements:
- Python 3.7+
- PaddleOCR and PaddlePaddle libraries
- Gemini API key for content extraction

### Example Output:
- **Brand Name**: XYZ Corp.
- **Expiry Date**: 12/31/2025


### original image 
![trail1](https://github.com/user-attachments/assets/5f6329cb-9a7b-4613-82d0-8769c55c4b8b)


### Preprocessed image


![WhatsApp Image 2024-10-20 at 7 55 25 PM](https://github.com/user-attachments/assets/2ecd2a15-1f02-4a3f-9a80-5dd6d38f5c5d)


OCR extracted(only few details extracted are shown here):
1. **Brand Name:** The Baker's Dozen
2. **Product Name:** Banana Walnut Cake
3. **Manufacturing Date:** 10/09/24 (September 10, 2024)
4. **Expiry Date:** 09/12/24 (December 9, 2024)
5. **Net Quantity:** 150g
6. **Price:** ₹185 (inclusive of all taxes) 
7. **Ingredient in grams:** (Note: The provided text lists ingredients by percentage, not grams. To convert, you would need to multiply the percentage by the net quantity (150g). However, it's challenging to do this accurately as the formatting is inconsistent.)

   * **Banana:** 19% of 150g = 28.5g
   * **Wholewheat Flour (Atta):** 14% of 150g = 21g
   * **Walnuts:** 13% of 150g = 19.5g
   * **Whole Egg Powder:**  (Percentage not specified)
   * **Banana Powder:** (Percentage not specified)
   * **Raisins:** (Percentage not specified)
   * **Agen:** (Percentage not specified)
   * **INS 500 (i) Preservative:** (Percentage not specified)
   * **INS 202, N:** (Percentage not specified)
  
## Task 3 
### Brand Logo Detection using YOLOv8
![test1_detected_logo](https://github.com/user-attachments/assets/5d38f070-27e0-4b28-9f6a-3eb3c1531188)

This task provides a framework for brand logo detection using the YOLOv8 model, an advanced deep-learning framework for efficient object detection.


### Summary of Work Done

The project focuses on detecting brand logos within images using the YOLOv8 model.

#### Installation Process

1. **Environment Setup**: The project requires a specific version of PyTorch along with related libraries like torchvision and torchaudio, which can be installed using `pip`. The command provided installs the necessary packages while ensuring compatibility with CUDA 11.6, which is important for utilizing GPU acceleration.

2. **Dependencies**: All other required libraries are installed from a `requirements.txt` file, simplifying the setup process.

3. **Model Weights Download**: The project includes pre-trained model weights that are crucial for brand logo detection. These weights are downloaded from provided links and organized into directories for easy access during inference.

---

### Brand-Logo Detection

The core functionality of the project is to detect brand logos within images. This is accomplished by executing a specific Python script, `main_detection_yolov8.py`, with parameters that specify the model to use and the image to analyze. The results of the detection are saved in a designated results directory.

#### Inference Process

- By running the detection script, users can leverage the power of YOLOv8 to perform inference on images containing brand logos. The model processes the input image and outputs the detected logos, demonstrating its ability to identify and localize logos in diverse contexts accurately.

### Yolov8 Counting Process & Verification with IR Sensor

- To count the number of objects we use YOLO-v8, which classifies the object into one of the classes from the classes present in the COCO dataset. We count the bounding boxes with a confidence score of more than 75 percent. We verify this count using an LM-393 IR sensor which is attached to the conveyor belt as shown in the video. As the object crosses the sensor, the count is updated and displayed on a LCD display.

---



