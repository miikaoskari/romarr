import React from 'react';
import logo from '../../assets/png/romarr-high-resolution-logo-white-transparent.png';
const Login = () => {
  return (
    <div className="ml-auto mr-auto mt-20 flex max-w-2xl scale-150 flex-col items-center justify-center ">
      <div className="w-full  rounded-2xl bg-gray-900 px-4 py-4 shadow-2xl">
        <img className="ml-auto mr-auto h-auto w-32 rounded-3xl object-contain p-2 shadow-sm" src={logo} alt="logo" />
        <div className="flex">
          <h1 className="text-xs uppercase text-primary-light">Username</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input placeholder="" className="w-full content-center rounded-2xl bg-gray-800 pl-2"></input>
        </div>
        <div>
          <h1 className="text-xs uppercase text-primary-light">Password</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input type="password" placeholder="" className="w-full content-center rounded-2xl  bg-gray-800 pl-2"></input>
        </div>
        <div className="flex justify-center pt-2">
          <button className="w-full rounded-2xl bg-gray-800  p-2 text-xs uppercase text-primary-light hover:bg-blue-400">
            Login
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;
