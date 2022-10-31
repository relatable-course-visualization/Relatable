import pic from "../images/RelatableIcon.png";
import Search from "./searchBar";
import "../stylings/header.css";

const Header = () => {
    return(
        <header id ="Header">
            <>
                <img src = {pic} className="App-pic" alt="pic" />
                <>Relatable</>
                <Search/>
            </>
        </header>
    );
}

export default Header