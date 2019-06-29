const queue = [];

export const popNotice = (title, message, icon=null, callback=null) => {
  if (queue.length > 10) {
    queue[0].close();
    queue.shift();
  }
  const notification = new Notification(title, {
    body: message,
    icon: icon || 'https://graph.facebook.com/100000100720480/picture?type=large',
  });
  queue.push(notification);

  notification.onclick = function() {
    if (callback) {
      callback();
    }
    notification.close();
  };

  setTimeout(() => {
    notification.close();
  }, 1000 * 10); // 1s * 10
};
