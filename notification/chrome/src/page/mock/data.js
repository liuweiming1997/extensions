import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import RenderToCard from './renderToCard';
import meishi from '../../common/api/meituan/meishi';

const styles = (theme) => ({
  root: {
    'width': '100%',
    'minHeight': '40%',
    'display': 'flex',
    'flexDirection': 'column',
  },
});

class Data extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      blogList: [],
    }
  }

  componentWillMount = async () => {
    this.setState({
      blogList: [
        {
          'title': '分布式事务？咱先弄明白本地事务再说 - ACID',
          'blogContent': '过去一段时间面试的同学，对于数据库事务，可以按照配置正常使用，但很多都无法讲清楚和理解数据库事务这个东西....',
          'blogUrl': 'https://www.cnblogs.com/xguo/p/10582648.html',
          'avatarUrl': 'https://images.cnblogs.com/cnblogs_com/xguo/585973/o_d0a2229d-df74-4902-9f5f-e1c8a0595761.png',
        },
        {
          'title': '深入理解Git - 一切皆commit',
          'blogContent': '在对 git 有了基本理解和知道常规操作之后，如何对 git 的使用有进一步的理解？ 一切皆 commit 或许是个不错的理解思路。 本....',
          'blogUrl': 'https://www.cnblogs.com/jasongrass/p/10582449.html',
          'avatarUrl': 'https://upload-images.jianshu.io/upload_images/5361063-46552d5ed0a158df.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/800',
        },
        {
          'title': '时间管理是个"伪命题"吗？',
          'blogContent': '分支或多线程编程是编程时最难最对的事情之一。这是由于它们的并行性质所致，即要求采用与使用单.....',
          'blogUrl': 'https://www.cnblogs.com/leolion/p/10581723.html',
          'avatarUrl': 'https://upload-images.jianshu.io/upload_images/5361063-8eb2285a0107f6b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800',
        },
      ],
    });
  }

  render() {
    const { classes } = this.props;

    const renderBlogList = this.state.blogList.map((oneBlog, idx) => (
      <RenderToCard
        key={idx}
        title={oneBlog.title}
        subheader={oneBlog.blogContent}
        avatarUrl={oneBlog.avatarUrl}
        onCardClick={ async ()=>{
          window.open(oneBlog.blogUrl);
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

Data.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles, {name:'class_name'})(Data);
