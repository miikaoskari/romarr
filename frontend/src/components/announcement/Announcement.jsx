import React from 'react';
import { FaExclamationTriangle } from 'react-icons/fa';

function Announcement() {
  return (
    <div className="m-0 flex h-min w-full items-center justify-center bg-gray-800 py-1 text-white ">
      <FaExclamationTriangle className="mr-2 mt-1 flex items-center justify-center" />
      <h1>
        During testing phase you need to get your own API-keys and put them into <strong>config.json</strong>
      </h1>
    </div>
  );
}

export default Announcement;
