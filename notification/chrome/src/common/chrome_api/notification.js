/*global chrome*/
export const chromeNotification = (title, message, callback) => {
  // console.log(chrome.notifications);
  chrome.notifications.create('notification_id', {
    type: 'basic',
    title: title,
    iconUrl: 'https://graph.facebook.com/100000100720480/picture?type=large',
    message: message,
  }, (notification_id) => {
    if (callback) {
      callback(notification_id);
    }
  });
};
