import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'height': '100%',
    'display': 'flex',
    'flexDirection': 'column',
  }
});

class MeishiPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      meishiList: [],
    }
  }

  componentWillMount = async () => {
    const response = await meishi.getAllMeishi();
    this.setState({
      meishiList: response,
    });
    console.log(this.state.meishiList);
  }

  render() {
    const { classes } = this.props;

    const renderMeishiList = this.state.meishiList.map((meishi, idx) => (
      <div>
        22222
      </div>
    ));

    return (
      <div className={classes.root}>
        {renderMeishiList}
      </div>
    );
  }
}

MeishiPage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(MeishiPage);
