import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import InfoIcon from '@material-ui/icons/Info';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';

const styles = (theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  icon: {
    color: 'rgba(255, 255, 255, 0.54)',
  },
  gridList: {
    width: '100%',
  },
  titleBar: {
    background:
      'linear-gradient(to bottom, rgba(0,0,0,0.7) 0%, ' +
      'rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
  },
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

  render() {
    const { classes } = this.props;
    return (
      <GridListTile key={this.props.img}>
        <img src={this.props.img} />
        <GridListTileBar
          title={this.props.title}
          subtitle={<span>{this.props.region + ' ' + this.props.score}</span>}
          actionIcon={
            <IconButton className={classes.icon}>
              <InfoIcon />
            </IconButton>
          }
        />
      </GridListTile>
    );
  }
}

RenderToCard.propTypes = {
  classes: PropTypes.object.isRequired,
  img: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  region: PropTypes.string.isRequired,
  score: PropTypes.string,
  onshowTime: PropTypes.string
};

export default withStyles(styles, {name:'class_name'})(RenderToCard);
