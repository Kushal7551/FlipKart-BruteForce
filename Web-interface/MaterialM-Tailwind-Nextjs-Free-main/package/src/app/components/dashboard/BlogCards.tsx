"use client";
import React from "react";
import Image from "next/image";
// import right
import user1 from "/public/images/profile/user-6.jpg";
import user2 from "/public/images/profile/user-2.jpg";
import user3 from "/public/images/profile/user-3.jpg";
import img1 from "/public/images/blog/blog-img1.jpg";
import img2 from "/public/images/blog/blog-img2.jpg";
import img3 from "/public/images/blog/blog-img3.jpg";
import img4 from "/public/images/blog/task1_2.png";
import img5 from "/public/images/blog/task2_2.png";
import img6 from "/public/images/blog/task3_2.jpg";
import img7 from "/public/images/blog/task3_1o.jpg";
import img8 from "/public/images/blog/task4_2.jpg";
import { Badge } from "flowbite-react";
import { TbPoint }   from "react-icons/tb";

import { Icon } from "@iconify/react";
import Link from "next/link";

const BlogCardsData = [
  {
    avatar: user1,
    coveravatar: img4,
    // read: "2 min Read",
    title: "OCR to extract details from image/label",
    category: "Extracting Details",
    name: "Georgeanna Ramero",
    view: "9,125",
    comments: "3",
    time: "Mon, Dec 19",
    url:'/sample-page'
  },
  {
    avatar: user2,
    coveravatar: img5,
    read: "2 min Read",
    title:
      "Using OCR to get expiry date details ",
    category: "Expiry Date Validation",
    name: "Georgeanna Ramero",
    view: "4,150",
    comments: "38",
    time: "Sun, Dec 18",
    url:'/sample-page2'
  },
  {
    avatar: user3,
    coveravatar: img6,
    read: "2 min Read",
    title: "Image recognition & IR based counting",
    category: "Brand Recognition and Count Confirmation",
    name: "Georgeanna Ramero",
    view: "9,480",
    comments: "12",
    time: "Sat, Dec 17",
    url:'/sample-page3'
  },
  {
    avatar: user3,
    coveravatar: img8,
    read: "2 min Read",
    title: "Detecting freshness of fresh produce",
    category: "Predicting Shelf Life",
    name: "Georgeanna Ramero",
    view: "9,480",
    comments: "12",
    time: "Sat, Dec 17",
    url:'/sample-page4'
  }
];

const BlogCards = () => {
  return (
    <>
      <div className="h-45 flex grid grid-cols-4 gap-30">
        {BlogCardsData.map((item, i) => (
          <div className="lg:col-span-2" key={i}>
            <Link href={item.url} className="group">
            <div className="rounded-lg dark:shadow-dark-md shadow-md bg-white dark:bg-darkgray p-0 relative w-3/4 break-words overflow-hidden">
                <div className="relative">
                  <Image src={item.coveravatar} alt="materialm" />
                  
                </div>

                <div className="px-6 pb-6">
                 
                  <Badge color={"muted"} className="mt-6">
                    {item.category}
                  </Badge>
                  <h5 className="text-lg my-6 group-hover:text-primary line-clamp-2">{item.title}</h5>
                  <div className="flex">

                    <div className="flex gap-1 items-center ms-auto">
                      {/* <TbPoint
                        size={15}
                        className="text-dark"
                      />{" "} */}
                      <span className="text-sm text-dark"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="size-6">
  <path fillRule="evenodd" d="M13.28 11.47a.75.75 0 0 1 0 1.06l-7.5 7.5a.75.75 0 0 1-1.06-1.06L11.69 12 4.72 5.03a.75.75 0 0 1 1.06-1.06l7.5 7.5Z" clipRule="evenodd" />
  <path fillRule="evenodd" d="M19.28 11.47a.75.75 0 0 1 0 1.06l-7.5 7.5a.75.75 0 1 1-1.06-1.06L17.69 12l-6.97-6.97a.75.75 0 0 1 1.06-1.06l7.5 7.5Z" clipRule="evenodd" />
</svg>
</span>
                    </div>
                  </div>
                </div>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </>
  );
};

export default BlogCards;
