import RequestBase from '../base';

class Meishi extends RequestBase {
  constructor() {
    super();
    this.getBlog();
  }
  getBlog = async () => {
    const response = await this.get('http://119.23.231.141:8888/blog/get_blog/aaa/1551839688/');
    console.log(response);
  }
};

const meishi  = new Meishi();

export default meishi;
