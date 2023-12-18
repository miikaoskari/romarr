const Activity = () => {
    return (
        <div>
            <div className={"flex flex-col items-center"}>
                <h1 className={"text-3xl font-bold"}>Queue</h1>
            </div>

            <div className={"mx-36 flex flex-col items-center bg-white rounded-2xl shadow-2xl border-2"}>
                <table className={"table-auto"}>
                    <thead>
                    <tr>
                        <th>Song</th>
                        <th>Artist</th>
                        <th>Year</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>
                        <td>Malcolm Lockyer</td>
                        <td>1961</td>
                    </tr>
                    <tr>
                        <td>Witchy Woman</td>
                        <td>The Eagles</td>
                        <td>1972</td>
                    </tr>
                    <tr>
                        <td>Shining Star</td>
                        <td>Earth, Wind, and Fire</td>
                        <td>1975</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
        ;
};

export default Activity;
