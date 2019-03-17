import React from 'react';
import PropTypes from 'prop-types';
import NotificationsIcon from '@material-ui/icons/Notifications';
import { withStyles } from '@material-ui/core/styles';
import { fade } from '@material-ui/core/styles/colorManipulator';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import SearchIcon from '@material-ui/icons/Search';
import ThreeSixtyIcon from '@material-ui/icons/ThreeSixty';
import Input from '@material-ui/core/Input';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import MailIcon from '@material-ui/icons/Mail';
import Avatar from '@material-ui/core/Avatar';
import AccountCircle from '@material-ui/icons/AccountCircle';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import DeleteIcon from '@material-ui/icons/Delete';
import AddIcon from '@material-ui/icons/Add';
import Tooltip from '@material-ui/core/Tooltip';
import SvgIcon from '@material-ui/core/SvgIcon';

import log from '../common/lib/log';
import account from '../common/account';
import mrouter from '../common/mrouter';

const styles = theme => ({
  main: {
    'display': 'flex',
    'flex-direction': 'row',
    'width': '100%',
    'height': '100%',
    'justify-content': 'flex-start',
    'align-items': 'flex-start',
  },
  appBar: {
    'display': 'flex',
    'flex-direction': 'row',
    'justify-content': 'space-between',
    'align-items': 'center',
    'width': '100%',
    'height': theme.spacing.unit * 6,
  },
  title: {
    'font-size': theme.spacing.unit * 3,
  },
  Search: {
    'display': 'flex',
    'flex-direction': 'row',
    'align-items': 'center',
    'color': 'white',
    backgroundColor: fade(theme.palette.common.white, 0.01),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
  },
  searchIcon: {
  },
  searchInput: {
    'margin-left': theme.spacing.unit,
    'color': 'white',
  },
  LogoUser: {
    'display': 'flex',
    'flex-direction': 'row',
    'align-items': 'center',
    'justify-content': 'space-between',
  },
  list: {
    'width': '100%',
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'justify-content': 'center',

  },
});

class AppTopBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      rightProfileOpenStatus: false,
    }
  }

  getRightProfileList() {
    const {classes} = this.props;
    const profileList = (
      <div className={classes.list}>
        <List>

          <ListItem button onClick={(e)=>{
            if (account.isLogin) {
              mrouter.goToIndexPage();
            } else {
              mrouter.goToLoginPage();
            }
          }}>
            <ListItemIcon><AccountCircle /></ListItemIcon>
            <ListItemText 
              primary="profile" 
            />
          </ListItem>

          <Divider />

          <ListItem button onClick={(e)=>{mrouter.goToWriteBlogPage()}}>
            <ListItemIcon><AddIcon /></ListItemIcon>
            <ListItemText primary="write blog" />
          </ListItem>

          <Divider />

          <ListItem button onClick={(e)=>{mrouter.goToLoginPage()}}>
            <ListItemIcon><DeleteIcon /></ListItemIcon>
            { account.isLogin ?
              <ListItemText primary="logout" /> : 
              <ListItemText primary="login" />
            }
          </ListItem>

        </List>
      </div>
    );
    return profileList;
  }

  componentWillMount() {
  }

  componentWillUnmount() {

  }

  openRightProfile() {
    this.setState({
      rightProfileOpenStatus: true,
    });
  }

  closeRightProfile() {
    this.setState({
      rightProfileOpenStatus: false,
    }); 
  }

  appTopBar() {
    const {classes} = this.props;

    const Title = () => (
      <div>
        <Tooltip title="Back to previous page"  onClick={(e)=>{mrouter.backOnePage()}}>
          <IconButton color="inherit">
            <ThreeSixtyIcon />
          </IconButton>
        </Tooltip>
      </div>
    );

    const Search = () => (
      <div className={classes.Search}>
        <SearchIcon className={classes.searchIcon}/>
        <Input
          id="input_search"
          onKeyDown={(e)=>{
            if (this.props.onBarKeyDown) {
              this.props.onBarKeyDown(e)}
            }
          }
          className={classes.searchInput}
          placeholder="search...."
        />
      </div>
    );

    const LogoUser = () => (
      <div className={classes.LogoUser}>

        <IconButton color="inherit">
          <Badge badgeContent={17} color="secondary">
            <NotificationsIcon />
          </Badge>
        </IconButton>

        <IconButton color="inherit">
          <Badge badgeContent={4} color="secondary">
            <MailIcon />
          </Badge>
        </IconButton>

        <IconButton color="inherit" onClick={(e)=>{this.openRightProfile(e)}}>
          { account.isLogin ? 
            <Avatar src={account.user.avatar}> {account.user.username[0]} </Avatar>
            :
            <AccountCircle />}
        </IconButton>

      </div>
    );

    const RightProfile = () => (
      <Drawer open={this.state.rightProfileOpenStatus} anchor="right"  onClick={(e)=>{this.closeRightProfile()}}>
        <div
          tabIndex={0}
          role="button"
        >
          {this.getRightProfileList()}
        </div>
      </Drawer>
    );

    const result = () => (
      <main className={classes.main}>
        <AppBar className={classes.appBar} position="static"> 
          <Title title={"Material-ui"} />
          {
            <Search />
          }
          <LogoUser />
          <RightProfile />
        </AppBar>
      </main>
    );
    return result();
  }

  render() {
    return (
      <div style={{"width":"100%"}}>
        {this.appTopBar()}
      </div>
    );
  }
}

AppTopBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(AppTopBar);
