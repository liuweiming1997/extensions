import RequestBase from '../base';

class Meishi extends RequestBase {
  constructor() {
    super();
  }
  getAllMeishi = async () => {
    return await this.get('/meituan/meishi/', {});
  }
};

const meishi  = new Meishi();

export default meishi;
