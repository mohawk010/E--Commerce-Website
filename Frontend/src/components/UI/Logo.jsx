import React from 'react'
import { GiGoat } from 'react-icons/gi'
import { Link } from 'react-router-dom'
import { LuShoppingBag } from "react-icons/lu";

const Logo = ({className}) => {
  return (
    <>
     <Link to={'/'} className={"flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0"+className}>
         <span className=' text-black'>
               <LuShoppingBag className='text-2xl' />
         </span>
      <span className="ml-3 text-xl">EcomFarm</span>
    </Link>
    </>
  )
}

export default Logo