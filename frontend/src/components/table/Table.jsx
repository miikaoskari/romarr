import React from 'react';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import propTypes from 'prop-types';

const Table = (data) => {
  const dataArray = Object.entries(data);
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
        {dataArray.map((item, index) => (
          <tr key={index} className={'border-b odd:bg-white even:bg-gray-50 even:dark:bg-gray-800'}>
            <td className={'whitespace-nowrap px-2 py-4 font-medium text-black'}>{item[1].title}</td>
            <td className={'px-2 py-4'}>{item[1].sourceTitle}</td>
            <td className={'px-2 py-4'}>{item[1].console}</td>
            <td className={'px-2 py-4'}>{item[1].date}</td>
            <td className={'px-2 py-4 text-right'}>
              <FontAwesomeIcon icon={faTrash} />
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

Table.propTypes = {
  data: propTypes.array,
};

export default Table;
