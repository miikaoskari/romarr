import React from 'react';
import { FaExclamationTriangle } from "react-icons/fa";

function Announcement() {
    return (
        <div className='bg-gray-800 text-white m-0 h-min flex items-center justify-center py-1 w-full '>
            <FaExclamationTriangle className='flex items-center justify-center mt-1 mr-2' />
            <h1>During testing phase you need to get your own API-keys and put them into <strong>config.json</strong></h1>
            </div>
    )
}



export default Announcement;
