import RequestBase from '../base';

class Meishi extends RequestBase {
  constructor() {
    super();
    this.get();
  }
};

const meishi  = new Meishi();

export default meishi;
