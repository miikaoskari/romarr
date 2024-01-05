import React from 'react';
import { Header, RoundedBox, Search, Sidebar } from '../index';
import { About, Activity, Dashboard, Games, Login, Settings } from '../../pages';
import { Link, useLocation } from 'react-router-dom';
import { Breadcrumbs } from '@mui/material';

const Layout = () => {
  const location = useLocation();
  let MainContent;

  switch (location.pathname) {
    case '/':
      MainContent = <Dashboard />;
      break;
    case '/about':
      MainContent = <About />;
      break;
    case '/activity':
      MainContent = <Activity />;
      break;
    case '/games':
      MainContent = <Games />;
      break;
    case '/settings':
      MainContent = <Settings />;
      break;
    case '/login':
      MainContent = <Login />;
      break;
    default:
      MainContent = <Dashboard />;
  }

  // Split the current path
  const pathnames = location.pathname.split('/').filter((x) => x);

  // Helper function to capitalize the first letter of each word
  const capitalize = (s) => {
    if (typeof s !== 'string') return '';
    return s.charAt(0).toUpperCase() + s.slice(1);
  };

  return (
    <div className="flex">
      <Sidebar />
      <RoundedBox>
        <Header>
          <Breadcrumbs aria-label={'breadcrumb'} className={'px-6'}>
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
