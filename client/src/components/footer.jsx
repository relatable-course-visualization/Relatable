import { Button, Container, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

// MUI's makeStyles hooks is used to add CSS
const useStyles = makeStyles({
  footer: {
    position: "absolute",
    bottom: 0,
    width: "100%",
    backgroundColor: "var(--clr-primary-color)",
  },

  footerButton: {
    textTransform: "none",
    fontFamily: "var(font-family)",
    fontSize: "var(--fs-3)",
    fontWeight: "var(--fw-bold)",
    "& .MuiButton-label": {
      whiteSpace: "nowrap", // prevents text going into multiple lines
    },

    // media queries
    "@media (max-width: 600px)": {
      fontSize: "var(--fs-4)",
    },
  },

  footerButtonGrid: {
    maxWidth: "130px",

    // media queries
    "@media (max-width: 600px)": {
      maxWidth: "100px",
    },
  },

  footerGrid: {
    "@media (max-width: 320px)": {
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
    },
  },
});

function Footer() {
  const classes = useStyles();

  return (
    <footer className={classes.footer}>
      <Container minWidth="md">
        <Grid
          alignItems="center"
          container
          justifyContent="center"
          spacing={4}
          className={classes.footerGrid}
        >
          <Grid item className={classes.footerButtonGrid}>
            <Button color="inherit" href="/" className={classes.footerButton}>
              Search
            </Button>
          </Grid>
          <Grid item className={classes.footerButtonGrid}>
            <Button
              color="inherit"
              href="/about-us"
              className={classes.footerButton}
            >
              About Us
            </Button>
          </Grid>
          <Grid item className={classes.footerButtonGrid}>
            <Button
              color="inherit"
              href="/contact-us"
              className={classes.footerButton}
            >
              Contact Us
            </Button>
          </Grid>
        </Grid>
      </Container>
    </footer>
  );
}

export default Footer;
