import React from 'react';
import '../stylings/navbar.css';
import RelatableLogo from '../images/relatable_full_logo.png';

function Navbar() {
  return (
    <>
      <nav className="navbar">
        <div className="navbar-container">
          <ul className="navbar-menu">
            <li className="navbar-logo">
              <img src={RelatableLogo} alt="Relatable Logo" id="logo" />
            </li>
            <div className="navbar-item-div">
              <li>
                <a href="/" className="navbar-links">
                  <p> Home</p>
                </a>
              </li>
              <li>
                <a href="/about-us" className="navbar-links">
                  <p>About Us</p>
                </a>
              </li>
            </div>
          </ul>
        </div>
      </nav>
    </>
  );
}

export default Navbar;
