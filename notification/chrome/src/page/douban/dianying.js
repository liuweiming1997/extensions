import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import RenderToCard from './renderToCard';
import dianying from '../../common/api/douban/dianying';

const styles = (theme) => ({
  root: {
    'minWidth': '100%',
    'minHeight': '40%',
    'display': 'flex',
    'flexDirection': 'column',
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
    const upcoming = await dianying.getUpcomingMovie();
    this.setState({
      onshowMovie: onshow,
      upcomingMovie: upcoming,
    });
  }

  render() {
    const { classes } = this.props;

    const renderMovie = () => (
      <RenderToCard
        key="123"
        theMovieOnshow={this.state.onshowMovie}
        theMovieUpcoming={this.state.upcomingMovie}
      />
    )

    return (
      <div className={classes.root}>
        {renderMovie()}
      </div>
    );
  }
}

DianyingPage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(DianyingPage);
