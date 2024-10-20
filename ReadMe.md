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



