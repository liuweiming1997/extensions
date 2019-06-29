import log from './lib/log';

class Singleton {
  constructor() {
    this.init_key = 'init';
    this.not_init_key = 'not_init';
    this.queue = [];
  }

  get(key) {
    return localStorage.getItem(key);
  }

  init(key) {
    localStorage.setItem(key, this.init_key);
    log.info(`Init key ${key}`);
    this.queue.push(key);
  }

  clear_init() {
    for (const idx in this.queue) {
      localStorage.setItem(this.queue[idx], this.not_init_key);
    }
  }

  isInit(key) {
    return this.get(key) === this.init_key;
  }
}

const singleton = new Singleton();

export default singleton;
