import React, { useEffect, useState } from 'react';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Table = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/api/v1/games')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setData(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <table className={'w-full text-left text-sm text-gray-500 rtl:text-right dark:text-gray-400'}>
      <thead className={'bg-gray-50 uppercase text-black'}>
        <tr>
          <th className="px-2 py-3">Title</th>
          <th className="px-2 py-3">Source Title</th>
          <th className="px-2 py-3">Console</th>
          <th className="px-2 py-3">Date</th>
          <th className={'px-2 py-3'}></th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index} className={'border-b odd:bg-white even:bg-gray-50 even:dark:bg-gray-800'}>
            <td className={'whitespace-nowrap px-2 py-4 font-medium text-black'}>{item.title}</td>
            <td className={'px-2 py-4'}>{item.sourceTitle}</td>
            <td className={'px-2 py-4'}>{item.console}</td>
            <td className={'px-2 py-4'}>{item.date}</td>
            <td className={'px-2 py-4 text-right'}>
              <FontAwesomeIcon icon={faTrash} />
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
