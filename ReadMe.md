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



### original image 
![original_image](https://github.com/user-attachments/assets/5c0c1efc-51e3-4cd4-a408-0ac30f98d623)

### preprocessed image

![final_preprocessed_image](https://github.com/user-attachments/assets/0f89231f-35f0-46fd-aedb-2bbb39d2882c)

OCR extracted:
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

![test1_detected_logo](https://github.com/user-attachments/assets/5d38f070-27e0-4b28-9f6a-3eb3c1531188)




