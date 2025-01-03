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
<details>
<summary> OLD WORK </summary>

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

- 
![image](https://github.com/user-attachments/assets/ff484302-bfe3-4011-9b7e-7e9f98518823)


### IR Counting

![ir_count_0](https://github.com/user-attachments/assets/a197d6d6-a8e0-400c-ac75-3be19923efe6)

![ir_count_1](https://github.com/user-attachments/assets/8327fc1a-0f42-432d-a1c9-dca849c786ab)


## TASK 4

### Dataset Preparation:
Method 1:
Prepared the dataset using a hardware setup which automatically clicks photos every 15 min for 7 days using Raspberry Pi based camera module.

![setup](https://github.com/user-attachments/assets/01982ceb-2a89-4f95-9df9-cd7f09e4d518)

Method 2 :
Used a time lapse video available on internet and segmented frames for different stages of the fruit’s life cycle.

### Solution
Used Yolo-v8 , Pretrained Alexnet with transfer learning to predict freshness index.Created a regression based freshness score (exponential) where 0 indicates the most fresh and 100 indicates rotten fruit.

![image](https://github.com/user-attachments/assets/589c4be1-50dd-47c9-9a4e-88d6e6fa66cc)

Here 64.32 means it should be consumed as soon as possible while other banana with 29 score means it has time to get rotten.



---
</details>

<details>
 <summary> CURRENT WORK </summary>

 ### Brand Recoginition and Expiry Details

 #### Approach 1

 <img width="2171" alt="Drawing" src="https://github.com/user-attachments/assets/f1ab3c29-fd41-4d67-91a2-12d91ef2c432" />

 #### Approach 2
 
![old_arch](https://github.com/user-attachments/assets/7340ab43-8519-48c3-a2a1-99ed8e61d178)

Some Results:

![brand_appr_result1](https://github.com/user-attachments/assets/2a4fada5-df6a-4cfd-b660-4a1329b3ab68)

![brand_appr_result2](https://github.com/user-attachments/assets/abaf647e-d2aa-487c-a6a6-253e97cca8b8)



 ### Item Counting

 #### Approach 1
 Finetuned YOLOv11 with custom dataset
 
 ![yolo_arch](https://github.com/user-attachments/assets/14f3ebf1-238f-4627-a7ba-9aab19326591)

 Some Results:
 
![yolo_counting](https://github.com/user-attachments/assets/073acee2-26bc-43a6-b400-b69f4a206f04)

Some failure:

![yolo_count1](https://github.com/user-attachments/assets/eb229a7c-7815-4c50-b8f8-9e1e6e1dc333)


 
 #### Approach 2

 ![architecture](https://github.com/user-attachments/assets/9f2dc237-fec3-41c6-8d1c-e03534331e67)

 
### Freshness Detection

#### Dataset preparation:

##### Method1:

Prepared the dataset using a hardware setup which automatically clicks photos
![gas_setup](https://github.com/user-attachments/assets/297bec73-952c-4f39-9c31-ccad66f096fe)

![gas_setup_fruits](https://github.com/user-attachments/assets/de03e9ca-a8f5-47e3-98a6-f10978bd7096)


######  Method 2:

Used a time lapse video available on internet and segmented frames for different stages of the fruit’s life cycle.

![time_lapse](https://github.com/user-attachments/assets/7c235cdd-2069-4929-b684-cbf9b5295f7d)


#### Approach 1

Created a regression based freshness score (exponential) where 0 indicates the most fresh and 100 indicates rotten fruit.

<img width="1803" alt="Drawing (1)" src="https://github.com/user-attachments/assets/2eea3ce6-7352-4d56-a41c-7ec11dc7b7bc" />

Some Results:

![test_fruit_alexnet](https://github.com/user-attachments/assets/0040319a-5963-48ae-b830-6601e0ac2582)

   

#### Approach 2
<img width="2161" alt="Drawing (3)" src="https://github.com/user-attachments/assets/b3fbeb91-f222-4404-aaf2-41b5f890569a" />

 
</details>
