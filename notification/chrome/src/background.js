import storageService from './common/chrome_api/storage';
import singleton from './common/singleton';

class BackgroundService {
  constructor() {
  }

  popNotice = (title, message, callback=null) => {
    const notification = new Notification(title, {
      body: message,
      icon: 'https://graph.facebook.com/100000100720480/picture?type=large',
    });
  
    notification.onclick = function() {
      if (callback) {
        callback();
      }
    };

    setTimeout(() => {
      notification.close();
    }, 3000);
  };

  run = () => {
    if (singleton.isInit('BackgroundService')) {
      return;
    }
    singleton.init('BackgroundService');

    this.popNotice('a', 'b');

    let val = 1;

    setInterval(() => {
      this.popNotice('a', val);
      val += 1;
    }, 7000);

    window.onbeforeunload=function () {
      singleton.clear_init();
      return false;
    }
    window.onunload=function () {
      singleton.clear_init();
      return false;
    }
  }
};

const backgroundService = new BackgroundService();

export default backgroundService;
