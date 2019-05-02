export const popNotice = (title, message, callback=null) => {
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
