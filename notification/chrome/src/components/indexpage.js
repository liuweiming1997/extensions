import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppTopBar from './apptopbar';
import MeishiPage from '../page/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'height': '100%',
    'display': 'flex',
    'flexDirection': 'column',
  },
  apptopbarcss: {
    'width': '100%',
  },
  contentlist: {
    'width': '100%',
    'height': '100%',
    'display': 'block',
    'overflow': 'scroll',
    'marginTop': '4%',
  },
});

class IndexPage extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <div className={classes.apptopbarcss}>
          <AppTopBar />
        </div>
        <div className={classes.contentlist}>
          <MeishiPage />
        </div>
      </div>
    );
  }
}

IndexPage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(IndexPage);
