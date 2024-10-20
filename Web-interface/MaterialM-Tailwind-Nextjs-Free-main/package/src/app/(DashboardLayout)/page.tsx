import React from "react";

import BlogCards from "../components/dashboard/BlogCards";
import Link from "next/link";

const page = () => {
  return (
    <>
      <div className="grid grid-cols-12 gap-30">

        <div className="col-span-12">
          <BlogCards />
        </div>
        <div className="col-span-12 text-center">
          {/* <p className="text-base">
            Design and Developed by{" "}
            <Link
              href="https://wrappixel.com"
              target="_blank"
              className="pl-1 text-primary underline decoration-primary" 
            >
              wrappixel.com
            </Link>
          </p> */}
        </div>
      </div>
    </>
  );
};

export default page;
