import storageService from './common/chrome_api/storage';

class BackgroundService {
  constructor() {
    this.isInit = false;
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
    if (this.isInit) {
      return;
    }
    this.isInit = true;
    this.popNotice('a', 'b');
    storageService.set({
      username: 'weimingliu',
      password: 'hello_world',
    });
    storageService.get({
      'username': {},
      'password': {},
    }, (result) => {
      alert(JSON.stringify(result));
    });
  }
};

const backgroundService = new BackgroundService();

export default backgroundService;
