import React from "react";
import Box from '@mui/material/Box';
import Button from '@material-ui/core/Button'

const Course = (props) => {
    console.log(props);

    return(
                <Box 
                    // component='span' 
                    sx={{ p: 2, border: '1px solid grey',
                    padding: '10px',
                    maxWidth: '300px',
                    '&:hover':{backgroundColor: 'pink'}, }}>
                    
                    <h1>{props.courseName} </h1>
                    <p>{props.courseDescription}</p>
                    <h2>Prerequisites</h2>
                    <p>
                        <Button variant="contained">
                            280
                        </Button>
                        <Button variant="contained">
                            270
                        </Button>
                        <Button variant="contained">
                            214
                        </Button>
                    </p>
                    
                    <h3>dependencies</h3>
                    <p>
                    <Button variant="contained">
                            410
                        </Button>
                        <Button variant="contained">
                            440
                        </Button>
                        <Button variant="contained">
                            480
                        </Button>
                    </p>
                    
                    
                </Box>

            // <Button>
            //     <h1>{props.courseName} </h1>
            //     <p>{props.courseDescription}</p>          
            // </Button>
    )
}

export default Course;