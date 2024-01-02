import React from 'react';
import {Link} from "react-router-dom";
import logo from '../../assets/png/logo_no_text_white.png'
import {faChartLine, faGamepad, faGear, faHome, faUser} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {SidebarItem} from "../index";


const Sidebar = () => {
    const [selectedLink, setSelectedLink] = React.useState("/");
    const handleLinkClick = (link) => {
        setSelectedLink(link)
    }
    return (
        <div
            className="bg-gray-800 text-white h-screen sticky top-0 px-6 py-4 flex flex-col justify-between flex-shrink-0">
            <div>
                <Link to="/" className={"mt-4 mb-10 mx-4"}>
                    <img className="w-12" src={logo} alt="logo"/>
                </Link>
                <div className={"my-2"}>
                    <FontAwesomeIcon icon={faHome} className={"text-xl text-white mx-2"}/>
                    <Link to="/about"
                          className={selectedLink === '/about' ? "text-xl my-4 mx-4 text-white" : "text-xl my-4 mx-4 text-gray-400"}
                          onClick={() => handleLinkClick('/about')}>
                        Home
                    </Link>
                </div>
                <div className={"my-2"}>
                    <FontAwesomeIcon icon={faChartLine} className={"text-xl text-white mx-2"}/>
                    <Link to="/activity"
                          className={selectedLink === '/activity' ? "text-xl my-4 mx-4 text-white" : "text-xl my-4 mx-4 text-gray-400"}
                          onClick={() => handleLinkClick('/activity')}>
                        Activity
                    </Link>
                </div>
                <div className={"my-2"}>
                    <FontAwesomeIcon icon={faGamepad} className={"text-xl text-white mx-2"}/>
                    <Link to="/games"
                          className={selectedLink === '/games' ? "text-xl my-4 mx-4 text-white" : "text-xl my-4 mx-4 text-gray-400"}
                          onClick={() => handleLinkClick('/games')}>
                        Games
                    </Link>
                </div>
                <div className={"my-2"}>
                    <FontAwesomeIcon icon={faGear} className={"text-xl text-white mx-2"}/>
                    <Link to="/settings"
                          className={selectedLink === '/settings' ? "text-xl my-4 mx-4 text-white" : "text-xl my-4 mx-4 text-gray-400"}
                          onClick={() => handleLinkClick('/settings')}>
                        Settings
                    </Link>
                </div>
            </div>
            <div>
                <FontAwesomeIcon icon={faUser} className={"text-xl text-white mx-2"}/>
                <Link to="/login"
                      className={selectedLink === '/settings' ? "text-xl my-4 mx-4 text-white" : "text-xl my-4 mx-4 text-white"}
                      onClick={() => handleLinkClick('/login')}>
                    User
                </Link>
            </div>
        </div>
    );
};

export default Sidebar;