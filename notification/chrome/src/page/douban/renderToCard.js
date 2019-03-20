import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import InfoIcon from '@material-ui/icons/Info';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';

import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';

const styles = (theme) => ({
  fileRoot: {
    'width': '100%',
    'height': '100%',
    'display': 'flex',
    'flexDirection': 'row',
  },
  Carousel: {
    'width': '250px',
    'minheight': '150px',
    // 'overflow': 'hidden',
  },
  img: {
    'width': '250px',
    'height': '350px',
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

  render() {
    const { classes } = this.props;
    const renderMovie = this.props.theMovieList.map((movie, idx) => (
      <div className={classes.img}>
        <img className={classes.img} src={movie.img} alt="None" />
        <h1 className="legend">Legend 1</h1>
      </div>
    ));
    
    return (
      <div className={classes.fileRoot}>
        <Carousel 
          className={classes.Carousel}
          showThumbs={false}
        >
          {renderMovie}
        </Carousel>
      </div>
    );
  }
}

RenderToCard.propTypes = {
  classes: PropTypes.object.isRequired,
  theMovieList: PropTypes.array.isRequired,
  // img: PropTypes.string.isRequired,
  // title: PropTypes.string.isRequired,
  // region: PropTypes.string.isRequired,
  // score: PropTypes.string,
  // onshowTime: PropTypes.string
};

export default withStyles(styles, {name:'class_name'})(RenderToCard);
