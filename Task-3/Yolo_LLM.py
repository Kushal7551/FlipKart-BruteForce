from __future__ import division
import time
import cv2
import torch 
import numpy as np
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image  
import io 

yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY is None:
    raise ValueError("Google API Key not found. Set it in your environment variables.")

genai.configure(api_key=GOOGLE_API_KEY)

def capture_image_from_ipwebcam(ip_address):
    camera_url = f"http://{ip_address}/shot.jpg"  
    try:
        img_resp = requests.get(camera_url, timeout=5)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        image = cv2.imdecode(img_arr, -1)
        if image is not None:
            return image
        else:
            print("Failed to capture image.")
            return None
    except requests.RequestException as e:
        print(f"Error accessing webcam: {e}")
        return None

def get_product_details(image, yolo_model):
    try:
        results = yolo_model(image)
        detections = results.pandas().xyxy[0] 

        products = {}
        for _, row in detections.iterrows():
            product_name = row['name']
            products[product_name] = products.get(product_name, 0) + 1
        
        return products
    except Exception as e:
        print(f"Error in YOLO detection: {e}")
        return {}

def analyze_image_with_generative_ai(image_path):
    try:
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
        pil_image = Image.open(io.BytesIO(img_bytes))
        response = genai.GenerativeModel(model_name="gemini-1.5-pro-latest").generate_content(
            [pil_image, "Just give me the brand name."]
        )
        if hasattr(response, 'candidates') and len(response.candidates) > 0:
            brand_name = response.candidates[0].content.parts[0].text.strip()
            return brand_name if brand_name else "Brand name not found."

    except Exception as e:
        print(f"Error analyzing image with Google Generative AI: {e}")
    
    return None

ip_address = '192.168.29.101:8080' 
product_count = {}
while True:
    image = capture_image_from_ipwebcam(ip_address)

    if image is not None:
        detected_products = get_product_details(image, yolo_model)
        
        if detected_products:
            print("\nDetected Products using YOLOv5:")
            for product, count in detected_products.items():
                product_count[product] = product_count.get(product, 0) + count
                print(f"{product_count[product]} {product}(s) detected.")
            image_path = "temp_analysis_image.jpg"
            cv2.imwrite(image_path, image)
            analysis_response = analyze_image_with_generative_ai(image_path)
            if analysis_response:
                print(f"Extracted Brand Name: {analysis_response}")
            else:
                print("No response received from the analysis.")
            cv2.imshow("Captured Image", image)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cv2.destroyAllWindows()
