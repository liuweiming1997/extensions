import storageService from './common/chrome_api/storage';
import singleton from './common/singleton';

import fetchDianYing from './fetchForNotificatoin/douban/dianying';

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
