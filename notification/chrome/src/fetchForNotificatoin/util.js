const queue = [];

export const popNotice = (title, message, icon=null, callback=null) => {
  if (queue.length > 3) {
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
      notification.close();
    }
  };

  setTimeout(() => {
    notification.close();
  }, 5000);
};
