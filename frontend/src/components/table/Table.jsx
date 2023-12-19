import React from 'react';

const Table = () => {
    return (
        <div>
            <div
                className={"relative overflow-x-auto sm:rounded-lg mx-36 flex flex-col items-center bg-white rounded-2xl shadow-2xl border-2"}>
                <table className={"w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400"}>
                    <thead className={"text-xs text-gray-700 uppercase bg-gray-50"}>
                    <tr>
                        <th className="px-2 py-3">Song</th>
                        <th className="px-2 py-3">Artist</th>
                        <th className="px-2 py-3">Year</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr className={"odd:bg-white even:bg-gray-50 even:dark:bg-gray-800 border-b"}>
                        <td className={"px-2 py-4 font-medium text-gray-900 whitespace-nowrap"}>The Sliding Mr. Bones
                            (Next Stop, Pottersville)
                        </td>
                        <td className={"px-2 py-4"}>Malcolm Lockyer</td>
                        <td className={"px-2 py-4"}>1961</td>
                    </tr>
                    <tr className={"odd:bg-white even:bg-gray-50 border-b"}>
                        <td className={"px-2 py-4 font-medium text-gray-900 whitespace-nowrap"}>Witchy Woman</td>
                        <td className={"px-2 py-4"}>The Eagles</td>
                        <td className={"px-2 py-4"}>1972</td>
                    </tr>
                    <tr className={"odd:bg-white even:bg-gray-50 border-b"}>
                        <td className={"px-2 py-4 font-medium text-gray-900 whitespace-nowrap"}>Shining Star</td>
                        <td className={"px-2 py-4"}>Earth, Wind, and Fire</td>
                        <td className={"px-2 py-4"}>1975</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Table;