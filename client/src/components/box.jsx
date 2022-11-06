import Box from '@mui/material/Box';


export const box = (props) => {
    return(
        <Box component='span' 
            sx={{ p: 2, border: '1px solid grey',
            padding: '10px',
            '&:hover':{backgroundColor: 'pink'}, }}>

            <>{props.course}</>
        </Box>
    )
}