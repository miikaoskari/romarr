import React from 'react';
import logo from '../../assets/png/romarr-high-resolution-logo-white-transparent.png';
const Login = () => {
  return (
    <div className="flex flex-col items-center justify-center max-w-2xl scale-150 ml-auto mr-auto mt-20 ">
      <div className="rounded-2xl  bg-gray-900 px-4 py-4 shadow-2xl w-full">
      <img className="w-32 h-auto object-contain p-2 rounded-3xl shadow-sm ml-auto mr-auto" src={logo} alt="logo" />
        <div className="flex">
          <h1 className="text-xs uppercase text-primary-light">Username</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input placeholder="" className="content-center rounded-2xl bg-gray-800 pl-2 w-full"></input>
        </div>
        <div>
          <h1 className="text-xs uppercase text-primary-light">Password</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input type="password" placeholder="" className="content-center rounded-2xl bg-gray-800  pl-2 w-full"></input>
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
