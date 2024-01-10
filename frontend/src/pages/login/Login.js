import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent2.0.png';
import React from 'react';
const Login = () => {
  return (
    <div className="flex h-screen flex-col items-center justify-center">
      <div className="rounded-2xl border-2 bg-white px-4 py-4 shadow-2xl">
        <img src={logo} alt="logo" className="my-2 w-48" />
        <div className="flex">
          <h1 className="text-xs uppercase text-gray-700">Username</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input placeholder="" className="content-center rounded-2xl border-2 bg-gray-50 pl-2"></input>
        </div>
        <div>
          <h1 className="text-xs uppercase text-gray-700">Password</h1>
        </div>
        <div className="my-2 flex justify-center">
          <input type="password" placeholder="" className="content-center rounded-2xl border-2 bg-gray-50 pl-2"></input>
        </div>
        <div className="flex justify-center pt-2">
          <button className="w-full rounded-2xl border-2 bg-gray-50 p-2 text-xs uppercase text-gray-700 hover:bg-blue-400">
            Login
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;
