import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';

import RenderToCard from './renderToCard';
import dianying from '../../common/api/douban/dianying';

const styles = (theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
    flexDirection: 'row',
  },
  gridList: {
    width: '100%',
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    flexDirection: 'row',
  },
});

class DianyingPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      onshowMovie: [],
      upcomingMovie: [],
    }
  }

  componentWillMount = async () => {
    const onshow = await dianying.getOnshowMovie();
    this.setState({
      onshowMovie: onshow,
    });
    // const upcoming = await dianying.getUpcomingMovie();
    // this.setState({
    //   upcomingMovie: upcoming,
    // });
  }

  render() {
    const { classes } = this.props;

    const renderOnshow = this.state.onshowMovie.map((movie, idx) => (
      <RenderToCard
        key={idx}
        img={movie.img}
        title={movie.title}
        region={movie.region}
        score={movie.score}
      />
    ));

    // const renderUpcoming = this.state.upcomingMovie.map((movie, idx) => (
    //   <RenderToCard
    //     key={idx}
    //   />
    // ));

    return (
      <div className={classes.root}>
        <GridList cellHeight={300} className={classes.gridList}>
          {renderOnshow}
        </GridList>
      </div>
    );
  }
}

DianyingPage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(DianyingPage);
