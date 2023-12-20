import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent2.0.png';
const Login = () => {
    return (
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh'}}>
            <div className="rounded-2xl shadow-2xl border-2 flex justify-center px-4 py-4 bg-white mx-96">
                <img src={logo} alt="logo" className="w-48"/>
                <h1>Login</h1>
            </div>
        </div>
    );
};

export default Login;