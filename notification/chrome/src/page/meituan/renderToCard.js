import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import SvgIcon from '@material-ui/core/SvgIcon';
import Avatar from '@material-ui/core/Avatar';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import Badge from '@material-ui/core/Badge';
import CardActions from '@material-ui/core/CardActions';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import red from '@material-ui/core/colors/red';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import Divider from '@material-ui/core/Divider';

import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'height': '20%',
    'display': 'flex',
    'flexDirection': 'column',
  }, 
  card: {
    'display': 'flex',
    'flexDirection': 'column',
    'width': '100%',
    'height': '100%',
  },
  CardHeader: {
    'width': '100%',
    'height': '100%',
    'text-overflow':'ellipsis',
    'overflow':'hidden',
    'white-space':'nowrap',
  },
  goodCard: {
    'marginRight': '25px',
    'marginTop': '5px',
    'justifyContent': 'space-between',
  }
});

class RenderToCard extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root} onClick={this.props.onCardClick}>
        <Card className={classes.card} key={this.props.title + this.props.subheader}>
          <CardHeader
            className={classes.CardHeader}
            avatar={
              <Avatar src={this.props.avatarUrl}> N </Avatar>
            }
            title={this.props.title}
            subheader={this.props.subheader}
            action={
              <IconButton className={classes.goodCard}>
                <Badge badgeContent={0} color="secondary">
                  <SvgIcon>
                    <path fill="#000000" d="M5,9V21H1V9H5M9,21A2,2 0 0,1 7,19V9C7,8.45 7.22,7.95 7.59,7.59L14.17,1L15.23,2.06C15.5,2.33 15.67,2.7 15.67,3.11L15.64,3.43L14.69,8H21C22.11,8 23,8.9 23,10V12C23,12.26 22.95,12.5 22.86,12.73L19.84,19.78C19.54,20.5 18.83,21 18,21H9M9,19H18.03L21,12V10H12.21L13.34,4.68L9,9.03V19Z" />
                  </SvgIcon>
                </Badge>
              </IconButton>
            }
          />
        </Card>
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
