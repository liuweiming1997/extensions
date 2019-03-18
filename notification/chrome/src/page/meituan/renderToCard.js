import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import Typography from '@material-ui/core/Typography';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import IconButton from '@material-ui/core/IconButton';
import ExpandMore from '@material-ui/icons/ExpandMore';
import Collapse from '@material-ui/core/Collapse';
import Divider from '@material-ui/core/Divider';
import ExpandLess from '@material-ui/icons/ExpandLess';
import StarBorder from '@material-ui/icons/StarBorder';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import TextField from '@material-ui/core/TextField';

import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'minHeight': '20%',
    'display': 'flex',
    'flexDirection': 'column',
    // 'overflow': 'auto',
  },
  text: {
    'width': '50%',
    'text-overflow':'ellipsis',
    'overflow':'hidden',
    'white-space':'nowrap',
  },
  avatar: {
    'width': '8%',
  },
  ExpandMore: {
    'display': 'flex',
    'flexDirection': 'row',
  }
});

class RenderToCard extends React.Component {
  constructor(props) {
    super(props);
    this.styleTemp = null;
    this.state = {
      open: 'none', 
    }
  }

  onMouseOver = (id) => {
    this.styleTemp = document.getElementById(id).style;
    document.getElementById(id).style.cursor="pointer";
  }

  onMouseOut = (id) => {
    document.getElementById(id).style = this.styleTemp;
  }

  handleExpandMoreToggle = () => {
    this.setState({
      open: this.state.open === 'none' ? false : 'none',
    });
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <List>
          <ListItem key={this.props.title + this.props.subheader}>

            <ListItemAvatar 
              className={classes.avatar}
              onClick={this.props.onCardClick}
              onMouseOver={() => {this.onMouseOver(this.props.avatarUrl);}}
              onMouseOut={() => {this.onMouseOut(this.props.avatarUrl);}}
              id={this.props.avatarUrl}
            >
              <Avatar alt="None" src={this.props.avatarUrl} />
            </ListItemAvatar>

            <ListItemText
              className={classes.text}
              primary={this.props.title}
              secondary={
                <React.Fragment>
                  {this.props.subheader}
                </React.Fragment>
              }
            />

            <IconButton aria-label="move" onClick={this.handleExpandMoreToggle}>
              {this.state.open === 'none' ? <ExpandMore /> : <ExpandLess />}
            </IconButton>
          </ListItem>

          <div style={{"display": this.state.open}}>
            <a href={this.props.avatarUrl} >  goto </a>
          </div>
        </List>
        <Divider />
      </div>
    );
  }
}

RenderToCard.propTypes = {
  classes: PropTypes.object.isRequired,
  title: PropTypes.string.isRequired,
  subheader: PropTypes.string.isRequired,
  createTime: PropTypes.string.isRequired,
  avatarUrl: PropTypes.string.isRequired,
  onCardClick: PropTypes.func.isRequired,
};

export default withStyles(styles, {name:'class_name'})(RenderToCard);
