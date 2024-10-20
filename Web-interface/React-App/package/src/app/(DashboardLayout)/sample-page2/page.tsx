"use client";
import React ,{useState,useEffect} from 'react';
import { Badge } from "flowbite-react";
import WebcamCapture from '../../(DashboardLayout)/cameraopen/page'; // Adjust path accordingly
import dayjs from 'dayjs';
import img1 from "/public/assets/banana3.jpg";
import Image from "next/image";
const imageDetails = {
  productName: "Banana Robusta",
  brandName: "Banana",

  category: "Fruit",
  productId: "I7U98kjn",
  unit: 4,
  seller:"Moonstone Ventures LLP, New Delhi Gadaipur-110030, India",

  title: "Banana Robusta",
  PackingDate: "12/10/2024",
  ExpiryDate: "31/10/2024",
};

// Helper function to parse date strings in DD/MM/YYYY format
const parseDate = (dateString: string) => {
  const [day, month, year] = dateString.split("/").map(Number);
  return new Date(year, month - 1, day);  // month is 0-indexed in JavaScript Date
};

const SamplePage = () => {
  // Parse the expiry date using the helper function
  const [showWebcam, setShowWebcam] = useState(true);

  useEffect(() => {
    // Set a timer to switch from the webcam to the product details after 10 seconds
    const timer = setTimeout(() => {
      setShowWebcam(false);
    }, 6000); // 10 seconds

    return () => clearTimeout(timer); // Clear the timer on component unmount
  }, []);
  const expiryDate = dayjs(parseDate(imageDetails.ExpiryDate));
  const today = dayjs();

  // Calculate the difference in days
  const daysLeft = expiryDate.diff(today, 'day');
  const monthsLeft = expiryDate.diff(today, 'month');

  let badgeContent = '';
  let badgeColor = '';

  // Check if the product is expired or if it's within 6 months
  if (daysLeft <= 0) {
    badgeContent = 'Expired';
    badgeColor = 'failure';
  } else if (monthsLeft < 1) {
    badgeContent = `${daysLeft} days left`;
    badgeColor = 'yellow';
  }
  else if(monthsLeft>=1 && monthsLeft <=3){
    badgeContent = `${monthsLeft} months left`;
    badgeColor = 'yellow';
  }
  else{
    badgeContent = `Has more than 3 months`;
    badgeColor = 'green';

  }

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
          alt={imageDetails.title}
        />
      </div>  
      <div className="md:w-1/2 p-8 md:p-12">
        <div className="bg-amber-200 rounded-lg shadow-sm p-8">
          <h2 className="text-3xl font-bold text-white-800 mb-6">{imageDetails.title}</h2>
          <div className="space-y-2">
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
              <span className="font-semibold">Manufacturing Date:</span> {imageDetails.PackingDate}
            </p>
            <p className="text-md text-gray-800">
              <span className="font-semibold">Expiry Date:</span> {imageDetails.ExpiryDate}
            </p>
            {badgeContent && (
              <Badge color={badgeColor} size="sm">
                {badgeContent}
              </Badge>
            )}
          </div>
        </div>
      </div>
    </div>
    )}
    </>
  );
};

export default SamplePage;


