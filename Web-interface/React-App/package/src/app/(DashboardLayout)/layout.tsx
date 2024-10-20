"use client";
import React from "react";
import Sidebar from "./layout/vertical/sidebar/Sidebar";
import Header from "./layout/vertical/header/Header";

export default function Layout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className="flex w-full min-h-screen pb-12">
      {/* <div className="page-wrapper flex w-full"> */}
        <div className=" w-full bg-lightgray dark:bg-dark pb-12">
          <Header />
          <div className={`px-6 py-40 mx-16`}   >
            {children}
          {/* </div> */}
        </div>
      </div>
    </div>
  );
}
