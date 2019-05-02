import RequestBase from '../base';

class DianYing extends RequestBase {
  constructor() {
    super();
  }
  getOnshowMovie = async () => {
    return await this.get('/douban/dianying/onshow/', {});
  }
  getUpcomingMovie = async () => {
    return await this.get('/douban/dianying/upcoming/', {});
  }
};

const dianying  = new DianYing();

export default dianying;
