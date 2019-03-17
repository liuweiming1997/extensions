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

class RenderToList extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        
      </div>
    );
  }
}

RenderToList.propTypes = {
  classes: PropTypes.object.isRequired,
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  createTime: PropTypes.string.isRequired,
  avatarUrl: PropTypes.string.isRequired,
};

export default withStyles(styles, {name:'class_name'})(RenderToList);
