import pic from "../images/RelatableIcon.png";
import "../stylings/header.css";

const Header = () => {
    return(
        <header id ="Header">
            <div className="header">
                <img src = {pic} className="App-pic" alt="pic" />
                <>Relatable</>
            </div>
        </header>
    );
}

export default Header