import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent2.0.png';
const Login = () => {
    return (
        <div className="flex flex-col h-screen justify-center items-center">
            <div className="rounded-2xl shadow-2xl border-2 px-4 py-4 bg-white">
                <img src={logo} alt="logo" className="w-48 my-2"/>
                <div className="flex">
                    <h1 className="text-xs text-gray-700 uppercase">Username</h1>
                </div>
                <div className="flex justify-center my-2">
                    <input placeholder="" className="rounded-2xl border-2 bg-gray-50 content-center pl-2"></input>
                </div>
                <div>
                    <h1 className="text-xs text-gray-700 uppercase">Password</h1>
                </div>
                <div className="flex justify-center my-2">
                    <input type="password" placeholder="" className="rounded-2xl border-2 bg-gray-50 content-center pl-2"></input>
                </div>
                <div className="flex justify-center pt-2">
                    <button className="text-xs text-gray-700 uppercase bg-gray-50 border-2 rounded-2xl p-2 hover:bg-blue-400 w-full">Login</button>
                </div>
            </div>
        </div>
    );
};

export default Login;