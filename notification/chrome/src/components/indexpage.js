import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppTopBar from './apptopbar';
import MeishiPage from '../page/meituan/meishi';
import Data from '../page/mock/data';
import DianyingPage from '../page/douban/dianying';

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
  fly: {
    'marginLeft': '62px',
  }
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
          <Data />
          <DianyingPage />
          <MeishiPage />
          <div className={classes.fly}>
            <p> 广州(CAN) --> 上海(虹桥国际机场)(SHA)  2019.4.1 570 </p>
            <p> 广州(CAN) --> 上海(虹桥国际机场)(SHA)  2019.4.2 570 </p>
            <p> 广州(CAN) --> 上海(虹桥国际机场)(SHA)  2019.4.3 570 </p>
            <p> 广州(CAN) --> 上海(虹桥国际机场)(SHA)  2019.4.4 510 </p>
          </div>
        </div>
      </div>
    );
  }
}

IndexPage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(IndexPage);
