import RequestBase from '../base';

class Programming extends RequestBase {
  constructor() {
    super();
  }
  getAllProgrammingBlog = async () => {
    return await this.get('/medium/programming/', {});
  }
};

const programming  = new Programming();

export default programming;
