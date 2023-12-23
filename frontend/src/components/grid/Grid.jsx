import React from 'react';
import zelda from '../../assets/samples/zelda.jpeg'
import odyssey from '../../assets/samples/odyssey.png'

const Grid = () => {
    return (
        <div>
            <div className={"mx-36 bg-white rounded-2xl shadow-2xl border-2 justify-center items-center"}>
                <div className={"grid grid-cols-5 gap-4 mx-3 justify-center"}>
                    {
                        // card style
                    }
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={zelda}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold truncate text-black block capitalize">The Legend of Zelda:
                            Breath of the
                            Wild</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={odyssey}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold text-black block capitalize">Mario Odyssey</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={odyssey}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold text-black block capitalize">Mario Odyssey</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={odyssey}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold text-black block capitalize">Mario Odyssey</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={odyssey}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold text-black block capitalize">Mario Odyssey</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={zelda}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold truncate text-black block capitalize">The Legend of Zelda:
                            Breath of the
                            Wild</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={zelda}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold truncate text-black block capitalize">The Legend of Zelda:
                            Breath of the
                            Wild</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>
                    <div className="bg-gray-50 rounded-2xl my-2 border-2 hover:shadow-2xl duration-100">
                        <img className={"object-cover h-80 w-72 object-cover rounded-2xl"} src={zelda}></img>
                        <span className="text-gray-400 ml-3 mr-3 uppercase text-xs">nintendo</span>
                        <p className="ml-3 text-lg font-bold truncate text-black block capitalize">The Legend of Zelda:
                            Breath of the
                            Wild</p>
                        <div className="flex items-center">
                            <p className="text-lg font-semibold text-black cursor-auto my-3"></p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    );
};

export default Grid;