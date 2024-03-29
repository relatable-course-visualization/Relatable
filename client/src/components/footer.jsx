import React from 'react';
import { Button, Container, Grid } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import RelatableLogo from '../images/relatable_full_logo.png';
import '../stylings/footer.css';

// MUI's makeStyles hooks is used to add CSS
// The image is styled in footer.css
const useStyles = makeStyles({
  footer: {
    bottom: 0,
    width: '100%',
    height: '150px',
    backgroundColor: 'var(--clr-primary-color)',
    position: 'relative', // Relative position allows it to be placed right after content before it
    marginTop: 'auto', // For search page when there are no results, it fills space
    '@media (max-width: 600px)': {
      maxHeight: '115px',
    },
  },

  footerButton: {
    textTransform: 'none',
    fontFamily: 'var(font-family)',
    fontSize: 'var(--fs-3)',
    fontWeight: 'var(--fw-bold)',
    '& .MuiButton-label': {
      whiteSpace: 'nowrap', // prevents text going into multiple lines
    },
    '&:hover': {
      color: 'black',
    },

    '@media (max-width: 600px)': {
      fontSize: 'var(--fs-4)',
    },
  },

  footerButtonGrid: {
    maxWidth: '130px',
    '@media (max-width: 600px)': {
      maxWidth: '100px',
    },
  },

  footerGrid: {
    '@media (max-width: 320px)': {
      display: 'flex',
      flexDirection: 'row',
      alignItems: 'center',
    },
  },
});

function Footer() {
  const classes = useStyles();

  return (
    <footer className={classes.footer}>
      <Container minWidth="md" className={classes.footerContainer}>
        <img src={RelatableLogo} alt="Relatable Logo" id="logo" />
        <Grid
          alignItems="center"
          container
          justifyContent="center"
          spacing={4}
          className={classes.footerGrid}
        >
          <Grid item className={classes.footerButtonGrid}>
            <Button href="/" className={classes.footerButton}>
              Search
            </Button>
          </Grid>
          <Grid item className={classes.footerButtonGrid}>
            <Button href="/about-us" className={classes.footerButton}>
              About Us
            </Button>
          </Grid>
          {/* We can bring back contact us at a later stage */}
          {/* <Grid item className={classes.footerButtonGrid}>
            <Button href="/contact-us" className={classes.footerButton}>
              Contact Us
            </Button>
          </Grid> */}
        </Grid>
      </Container>
    </footer>
  );
}

export default Footer;
