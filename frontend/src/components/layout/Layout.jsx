import React from 'react';
import { Header, RoundedBox, Search, Navbar, Announcement } from '../index';
import { About, Activity, Dashboard, Games, Login, Settings, Home } from '../../pages';
import { Link, useLocation } from 'react-router-dom';
import { Breadcrumbs } from '@mui/material';

const Layout = () => {
  const location = useLocation();

  const routes = {
    '/': <Dashboard />,
    '/about': <About />,
    '/activity': <Activity />,
    '/games': <Games />,
    '/settings': <Settings />,
    '/login': <Login />,
    '/home': <Home />,
  };

  const MainContent = routes[location.pathname] || <Dashboard />;

  // Split the current path
  const pathnames = location.pathname.split('/').filter((x) => x);

  // Helper function to capitalize the first letter of each word
  const capitalize = (s) => {
    if (typeof s !== 'string') return '';
    return s.charAt(0).toUpperCase() + s.slice(1);
  };

  return (
    <div className="">
      <Announcement />
      <Navbar />
      <RoundedBox>
        <Header>
          <Breadcrumbs aria-label={'breadcrumb'} className="w-max rounded-3xl bg-gray-900 px-4 py-2 ">
            {' '}
            <Link to="/">Home</Link>
            {pathnames.map((value, index) => {
              const to = `/${pathnames.slice(0, index + 1).join('/')}`;

              return (
                <Link key={to} to={to}>
                  {capitalize(value)}
                </Link>
              );
            })}
          </Breadcrumbs>
          <Search />
        </Header>

        {MainContent}
      </RoundedBox>
    </div>
  );
};

export default Layout;
