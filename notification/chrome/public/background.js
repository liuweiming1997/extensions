/*global chrome*/
// chromeNotification = (title, message, callback) => {
//   // console.log(chrome.notifications);
//   chrome.notifications.create('notification_id', {
//     type: 'basic',
//     title: title,
//     iconUrl: 'https://graph.facebook.com/100000100720480/picture?type=large',
//     message: message,
//   }, (notification_id) => {
//     if (callback) {
//       callback(notification_id);
//     }
//   });
// };

// chromeNotification('a', 'b');

// setInterval(() => {
//   chromeNotification('s', 'b');
// }, 5000);

const popNotice = (title, message, callback=null) => {
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

popNotice('hello', 'test for');
