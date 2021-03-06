import storageService from './common/chrome_api/storage';
import singleton from './common/singleton';

import fetchDianYing from './fetchForNotificatoin/douban/dianying';
import fetchProgramming from './fetchForNotificatoin/medium/programming';

class BackgroundService {
  constructor() {
  }

  run = () => {
    if (singleton.isInit('BackgroundService')) {
      return false;
    }
    singleton.init('BackgroundService');

    // register any service
    fetchDianYing.init();
    fetchProgramming.init();
    // register any service
  
    window.onbeforeunload=function () {
      singleton.clear_init();
      return false;
    }
    window.onunload=function () {
      singleton.clear_init();
      return false;
    }
    return true;
  }
};

const backgroundService = new BackgroundService();

export default backgroundService;
