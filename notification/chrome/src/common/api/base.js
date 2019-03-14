import log from '../lib/log';

export default class RequestBase {
  constructor() {
  }
  get = () => {
    log.error('use get method');
  }
  post = () => {}
  put = () => {}
  del = () => {}
  options = () => {}
};
