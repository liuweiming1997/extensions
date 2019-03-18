import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import RenderToCard from './renderToCard';
import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'height': '100%',
    'display': 'block',
    'overflow': 'scroll',
  },
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
  }

  render() {
    const { classes } = this.props;

    const renderMeishiList = this.state.meishiList.map((oneMeishi, idx) => (
      <RenderToCard
        title={oneMeishi.title}
        subheader={oneMeishi.address}
        createTime={oneMeishi.createTime}
        avatarUrl={oneMeishi.frontImg}
        onCardClick={()=>{alert(oneMeishi)}}
      />
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
