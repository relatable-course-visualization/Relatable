import pic from "../images/RelatableIcon.png";
import Search from "./searchBar";

const Header = () => {
    return(
        <header className='header'>
            <>
                <img src = {pic} className="App-pic" alt="pic" />
                <>Relatable</>
                <Search/>
            </>
        </header>
    );
}

export default Header