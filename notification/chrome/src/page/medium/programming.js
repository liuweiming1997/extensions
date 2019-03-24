import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import RenderToCard from './renderToCard';
import programming from '../../common/api/medium/programming';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'minHeight': '40%',
    'display': 'flex',
    'flexDirection': 'column',
  },
});

class Programming extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      blogList: [],
    }
  }

  componentWillMount = async () => {
    const response = await programming.getAllProgrammingBlog();
    this.setState({
      blogList: response,
    });
  }

  render() {
    const { classes } = this.props;

    const renderBlogList = this.state.blogList.map((oneBlog, idx) => (
      <RenderToCard
        key={idx}
        title={oneBlog.title}
        url={oneBlog.url}
        onCardClick={ async ()=>{
          window.open(oneBlog.url);
        }}
      />
    ));

    return (
      <div className={classes.root}>
        {renderBlogList}
      </div>
    );
  }
}

Programming.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(Programming);
