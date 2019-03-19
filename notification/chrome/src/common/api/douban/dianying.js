import RequestBase from '../base';

class Meishi extends RequestBase {
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

const meishi  = new Meishi();

export default meishi;
