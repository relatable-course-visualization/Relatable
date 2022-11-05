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

    return ( 
        <div className="search">
            <div className="searchInputs">
                <input type="text" placeholder={placeholder} value={wordEntered} onChange={handleFilter}/>
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
                        return (<a className='dataItem'> 
                            <p>{value.class_name}</p>
                    
                            </a> 
                        )})}
                </div>
            )}
        </div>
    
    )    
}


// function SearchBar({ placeholder, data }) {
//     const [filteredData, setFilteredData] = useState([]);
//     const [wordEntered, setWordEntered] = useState("");
  
//     const handleFilter = (event) => {
//       const searchWord = event.target.value;
//       setWordEntered(searchWord);
//       const newFilter = data.filter((value) => {
//         return value.class_name.toLowerCase().includes(searchWord.toLowerCase());
//       });
  
//       if (searchWord === "") {
//         setFilteredData([]);
//       } else {
//         setFilteredData(newFilter);
//       }
//     };
  
//     const clearInput = () => {
//       setFilteredData([]);
//       setWordEntered("");
//     };
  
//     return (
//       <div className="search">
//         <div className="searchInputs">
//           <input
//             type="text"
//             placeholder={placeholder}
//             value={wordEntered}
//             onChange={handleFilter}
//           />
//           <div className="searchIcon">
//             {filteredData.length === 0 ? (
//               <SearchIcon />
//             ) : (
//               <CloseIcon id="clearBtn" onClick={clearInput} />
//             )}
//           </div>
//         </div>
//         {filteredData.length != 0 && (
//           <div className="dataResult">
//             {filteredData.slice(0, 15).map((value, key) => {
//               return (
//                 <a className="dataItem" href={value.link} target="_blank">
//                   <p>{value.class_name} </p>
//                 </a>
//               );
//             })}
//           </div>
//         )}
//       </div>
//     );
//   }
  
  export default SearchBar;