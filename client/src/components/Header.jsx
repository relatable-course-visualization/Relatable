import pic from "../images/RelatableIcon.png";
import "../stylings/header.css";

const Header = () => {
    return(
        <div className="header">
            <img src = {pic} className="App-pic" alt="pic" />
            <>Relatable</>
        </div>
    );
}

export default Header