import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'height': '20%',
    'display': 'flex',
    'flexDirection': 'column',
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
});

class RenderToCard extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root} onClick={this.props.onCardClick}>
        <List>
          <ListItem>

            <ListItemAvatar className={classes.avatar}>
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

          </ListItem>
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
