import pic from "../images/RelatableIcon.png";
import "../stylings/header.css";

const Header = () => {
    return(
        <header id ="Header">
            <>
                <img src = {pic} className="App-pic" alt="pic" />
                <>Relatable</>
            </>
        </header>
    );
}

export default Header