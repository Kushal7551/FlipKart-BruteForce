"use client";
import React, { useEffect, useState } from 'react';
import WebcamCapture from '../../(DashboardLayout)/cameraopen/page'; // Adjust path accordingly
import { Badge } from "flowbite-react";
import img1 from "/public/assets/banana3.jpg";
import Image from "next/image";
const imageDetails = {
  productName: "Banana Walnut Cake",
  brandName: "The Baker's Dozen",
  description: "Green skin that turns yellow as it ripens and has creamy white flesh inside.",
  mrp: "₹185 (inclusive of all taxes)",
  category: "Fruit",
  productId: "I7U98kjn",
  unit: 4,
  seller:"Moonstone Ventures LLP, New Delhi Gadaipur-110030, India",
  mfg:"10/09/24 (September 10, 2024)",
  exp:"09/12/24 (December 9, 2024)",
  nq:"150g",
  banana:"19% of 150g = 28.5g",
  Wholewheat:"14% of 150g = 21g",
  Walnuts:"13% of 150g = 19.5g",
  egg:"(Percentage not specified)",
  bananapowder:"(Percentage not specified)",
  raisins:"(Percentage not specified)",
  agen:"(Percentage not specified)",
  // src:
};

// 1. **Brand Name:** The Baker's Dozen
// 2. **Product Name:** Banana Walnut Cake
// 3. **Manufacturing Date:** 10/09/24 (September 10, 2024)
// 4. **Expiry Date:** 09/12/24 (December 9, 2024)
// 5. **Net Quantity:** 150g
// 6. **Price:** ₹185 (inclusive of all taxes) 
// 7. **Ingredient in grams:** (Note: The provided text lists ingredients by percentage, not grams. To convert, you would need to multiply the percentage by the net quantity (150g). However, it's challenging to do this accurately as the formatting is inconsistent.)

//    * **Banana:** 19% of 150g = 28.5g
//    * **Wholewheat Flour (Atta):** 14% of 150g = 21g
//    * **Walnuts:** 13% of 150g = 19.5g
//    * **Whole Egg Powder:**  (Percentage not specified)
//    * **Banana Powder:** (Percentage not specified)
//    * **Raisins:** (Percentage not specified)
//    * **Agen:** (Percentage not specified)
//    * **INS 500 (i) Preservative:** (Percentage not specified)
//    * **INS 202, N:** (Percentage not specified) 

const SamplePage = () => {
  const [showWebcam, setShowWebcam] = useState(true);

  useEffect(() => {
    // Set a timer to switch from the webcam to the product details after 10 seconds
    const timer = setTimeout(() => {
      setShowWebcam(false);
    }, 6000); // 10 seconds

    return () => clearTimeout(timer); // Clear the timer on component unmount
  }, []);

  return (
    <>
      {showWebcam ? (
        <WebcamCapture /> // Display WebcamCapture for 10 seconds
      ) : (
        <div className="max-w-6xl mx-auto bg-amber-100 rounded-xl shadow-lg overflow-hidden m-6 flex flex-col md:flex-row">
          <div className="md:w-1/2">
            <Image
              className="w-full h-full object-cover"
              src={img1}
              alt={imageDetails.productName}
            />
          </div>
          <div className="md:w-1/2 p-8 md:p-12">
            <div className="rounded-lg shadow-sm p-8 bg-amber-200">
              <h2 className="text-3xl font-bold text-white-800 mb-6">{imageDetails.productName}</h2>
              <p className="text-lg text-gray-600 mb-6 leading-relaxed">{imageDetails.description}</p>
              <div className="space-y-1.5">
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Name:</span> {imageDetails.brandName}
                </p>
                 <p className="text-md text-gray-800">
                  <span className="font-semibold">Product ID:</span> {imageDetails.productId}
                </p>                
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Category:</span> {imageDetails.category}
                </p>
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Unit:</span> {imageDetails.unit} pieces
                </p>               
                <p className="text-md text-gray-800">
                  <span className="font-semibold">MRP:</span> {imageDetails.mrp}
                </p>               
                 <p className="text-md text-gray-800">
                  <span className="font-semibold">Seller:</span> {imageDetails.seller}
                </p>
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Manufactured Date:</span> {imageDetails.mfg}
                </p>
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Expiry Date:</span> {imageDetails.exp}
                </p>
                <p className="text-md text-gray-800">
                  <span className="font-semibold">Net Quantity:</span> {imageDetails.nq}
                </p>
                <h3 className="text-md text-gray-800 font-semibold">Ingredient in grams:</h3>
                <p className="text-md text-gray-800 pl-4">
                  <span className="font-semibold">Banana:</span> {imageDetails.banana}
                </p>
                <p className="text-sm text-gray-800  pl-4">
                  <span className="font-semibold">Wholewheat Flour (Atta):</span> {imageDetails.Wholewheat}
                </p>
                <p className="text-sm text-gray-800 pl-4">
                  <span className="font-semibold">Walnuts:</span> {imageDetails.Walnuts}
                </p>

                <p className="text-sm text-gray-800 pl-4">
                  <span className="font-semibold">Whole Egg Powder:</span> {imageDetails.egg}
                </p>
                <p className="text-sm text-gray-800 pl-4">
                  <span className="font-semibold">Banana Powder:</span> {imageDetails.bananapowder}
                </p>
                <p className="text-sm text-gray-800 pl-4">
                  <span className="font-semibold">Raisins:</span> {imageDetails.raisins}
                </p>
                <p className="text-sm text-gray-800 pl-4">
                  <span className="font-semibold">Agen:</span> {imageDetails.agen}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default SamplePage;
