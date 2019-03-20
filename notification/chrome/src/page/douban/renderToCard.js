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
    'justifyContent': 'space-between',
  },
  Carousel: {
    'width': '250px',
    'minheight': '150px',
    // 'overflow': 'hidden',
  },
  img: {
    'width': '250px',
    'height': '350px',
  },
  legend: {
    display: 'flex',
    flexDirection: 'column',
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

  handleClick = (url) => {
    window.open(url);
  }

  render() {
    const { classes } = this.props;

    const showModal = (movie) => (
      <div 
        className="legend"
        id={movie.title}
        onMouseOver={()=>{this.onMouseOver(movie.title)}}
        onMouseOut={()=>{this.onMouseOut(movie.title)}}
        onClick={() => {this.handleClick(movie.buyTicket)}}
      >
        <span style={{"display": "block"}}> {movie.title}</span>
        <span> {movie.region}</span>
        <span> {movie.score}</span>
        {
          movie.onShowTime && 
          <span style={{"display": "block"}}> {movie.onShowTime}</span>
        }
      </div>
    )

    const renderOnshow = this.props.theMovieOnshow.map((movie, idx) => (
      <div 
        className={classes.img}
        id={movie.url}
        onMouseOver={()=>{this.onMouseOver(movie.url)}}
        onMouseOut={()=>{this.onMouseOut(movie.url)}}
        onClick={() => {this.handleClick(movie.url)}}
      >
        <img 
          className={classes.img} 
          src={movie.img}
          alt="None" />
        {showModal(movie)}
      </div>
    ));

    const renderUpcoming = this.props.theMovieUpcoming.map((movie, idx) => (
      <div 
        className={classes.img}
        id={movie.url}
        onMouseOver={()=>{this.onMouseOver(movie.url)}}
        onMouseOut={()=>{this.onMouseOut(movie.url)}}
        onClick={() => {this.handleClick(movie.url)}}
      >
        <img className={classes.img} src={movie.img} alt="None" />
        {showModal(movie)}
      </div>
    ));

    return (
      <div className={classes.fileRoot}>
        <Carousel 
          className={classes.Carousel}
          showThumbs={false}
          showIndicators={false}
          autoPlay
          stopOnHover
        >
          {renderOnshow}
        </Carousel>

        <Carousel 
          className={classes.Carousel}
          showThumbs={false}
          showIndicators={false}
          autoPlay
          stopOnHover
        >
          {renderUpcoming}
        </Carousel>

      </div>
    );
  }
}

RenderToCard.propTypes = {
  classes: PropTypes.object.isRequired,
  theMovieOnshow: PropTypes.array.isRequired,
  theMovieUpcoming: PropTypes.array.isRequired,
  // img: PropTypes.string.isRequired,
  // title: PropTypes.string.isRequired,
  // region: PropTypes.string.isRequired,
  // score: PropTypes.string,
  // onshowTime: PropTypes.string
};

export default withStyles(styles, {name:'class_name'})(RenderToCard);
