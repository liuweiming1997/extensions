import React from 'react';

import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';
import green from '@material-ui/core/colors/green';
import Tooltip from '@material-ui/core/Tooltip';
import LockIcon from '@material-ui/icons/LockOutlined';

import mrouter from '../common/mrouter';
import user from '../common/api/user/user';
import account from '../common/account';

const styles = theme => ({
  main: {
    backgroundColor: green[700],
    width: 'auto',
    display: 'block', // Fix IE 11 issue.
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(400 + theme.spacing.unit * 3 * 2)]: {
      width: 400,
      marginLeft: 'auto',
      marginRight: 'auto',
    },
  },
  paper: {
    marginTop: theme.spacing.unit * 8,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: `${theme.spacing.unit * 2}px ${theme.spacing.unit * 3}px ${theme.spacing.unit * 3}px`,
  },
  avatar: {
    margin: theme.spacing.unit,
    backgroundColor: green[500],
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing.unit,
  },
  submit: {
    marginTop: theme.spacing.unit * 3,
  },
  tooltip: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    boxShadow: theme.shadows[1],
    fontSize: 16,
  }
});

class Login extends React.Component {
  constructor(props) {
    super(props);
    if (account.isLogin) {
      mrouter.goToIndexPage();
    }
  }

  onUserLogin = async () => {
    const args = {
      username: document.getElementById('username').value,
      password: document.getElementById('password').value
    };
    if (!(args.username && args.password)) {
      return;
    }
    const response = await user.loadOrCreate(args.username, args.password);
    mrouter.goToIndexPage();
  }

  render() {
    const { classes } = this.props;
    return (
      <main className={classes.main}>
        <CssBaseline />
        <Paper className={classes.paper}>
          <Avatar className={classes.avatar} >
            <LockIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <form className={classes.form}>
            <FormControl margin="normal" required fullWidth>
              <InputLabel>Username</InputLabel>
              <Input id="username" type="text" name="username" autoFocus autoComplete="username" placeholder="your username"/>
            </FormControl>
            <FormControl margin="normal" required fullWidth>
              <InputLabel>Password</InputLabel>
              <Input 
                id="password" 
                name="password" 
                type="password" 
                autoComplete="current-password"
                placeholder="your password"
              />
            </FormControl>
            <Tooltip title="Confirm To Sing In" classes={{ tooltip: classes.tooltip }}>
              <Button
                type="button"
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
                onClick={()=>{this.onUserLogin();}}
              >
                Sign in
              </Button>
            </Tooltip>
          </form>
        </Paper>
      </main>
    );
  }
};

export default withStyles(styles, {name:'class_name'})(Login);
