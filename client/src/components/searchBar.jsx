import '../stylings/searchBar.css'
import SearchIcon from '@mui/icons-material/Search';
import CloseIcon from '@mui/icons-material/Close';
import { useState } from 'react';

function SearchBar({placeholder, data})  {

    const [filteredData, setFilteredData] = useState([])
    const [wordEntered, setWordEntered] = useState("")

    const handleFilter = (event) =>{
        const searchWord = event.target.value
        setWordEntered(searchWord)
        const newFilter = data.filter((value)=> {
            return value.class_name.toLowerCase().includes(searchWord.toLowerCase())
        })

        if(searchWord===""){
            setFilteredData([])
        } else{
            setFilteredData(newFilter)
        }
    }

    const clearSearch = () =>{
        setFilteredData([])
        setWordEntered("")
    }

    // onClickSubmit(e){
    //     e.preventDefault();
    //     alert("clicked");
    // }


    return ( 
        <div className="search">
            <div className="searchInputs">
                <input type="text" 
                placeholder={placeholder} 
                value={wordEntered} 
                onChange={handleFilter}
            />
                <div className="searchIcon">
                    {filteredData.length === 0 ? (
                        <SearchIcon/>
                    ) : (
                        <CloseIcon id="clearBtn" onClick =  {clearSearch}/>
                    )}
                </div>
            </div>

            {filteredData.length !==0 && (
                <div className="dataResult">
                    {filteredData.slice(0,15).map((value,key)=>{
                        return (
                        <a className='dataItem' href={value.description} rel="noopener"> 
                            <a href="#1" onclick="resetHref();">Content</a>
                            <a>{value.class_name}</a> 
                            <a>{value.description}</a>
                            <a>{value.prerequisites}</a>
                            <a>{value.dependencies}</a>
                            
                        </a>
                        )
                    })}
                </div>
                
            )}


        </div>
    
    )    
}
  
  export default SearchBar;