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
    this.popNotice('a', 'b');
    let a = 1;
    setInterval(() => {
      this.popNotice('a', a);
      a += 1;
    }, 4000);
  }
};

const backgroundService = new BackgroundService();

export default backgroundService;
