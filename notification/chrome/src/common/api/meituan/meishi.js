import RequestBase from '../base';

class Meishi extends RequestBase {
  constructor() {
    super();
  }
  getAllMeishi = async () => {
    return await this.get('/meituan/meishi/', {});
  }
  getUrl = async (poiId) => {
    return await this.get(`/meituan/meishi/${poiId}/`);
  }
};

const meishi  = new Meishi();

export default meishi;
