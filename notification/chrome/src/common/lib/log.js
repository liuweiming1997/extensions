const { getNowTimeString } = require('./dateUtil.js');

class logging {
  constructor() {
    this.info('log service start!');
  }

  convertMsgAndLog(msg, level) {
    const logMsg = {
      level: level,
      msg: msg,
      time: getNowTimeString(),
    };
    console.log(logMsg);
  }

  info(msg) {
    this.convertMsgAndLog(msg, 'info');
  }

  debug(msg) {
    this.convertMsgAndLog(msg, 'debug');
  }

  error(msg) {
    this.convertMsgAndLog(msg, 'error');
  }
};

const log = new logging();
export default log;
