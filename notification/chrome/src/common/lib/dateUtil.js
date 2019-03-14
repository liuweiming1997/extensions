// 0 --> sunday, 1 --> monday, ... 6 -> staurday
function getWeekString(date = null) {
  const today = !date ? new Date() : date;
  return '' + today.getDay();
}

function getNowTimeStamp() {
  return Date.now();
}


function getNowTimeString() {
  return formatTime(getNowTimeStamp());
}

function formatTime(ms) {
  const date = new Date(ms);
  const month = formatByDigits(date.getMonth() + 1);
  const day = formatByDigits(date.getDate());
  const hours = formatByDigits(date.getHours());
  const minutes = formatByDigits(date.getMinutes());
  const seconds = formatByDigits(date.getSeconds());
  const millisecond = formatByDigits(date.getMilliseconds(), 3);
  return `${date.getFullYear()}-${month}-${day} ${hours}:${minutes}:${seconds}.${millisecond}`;
}

function formatByDigits(number, digits = 2) {
  if (typeof(number) !== 'number') {
    return '000';
  }
  return `00${number}`.slice(-digits);
}

module.exports = {
  getWeekString: getWeekString,
  getNowTimeStamp: getNowTimeStamp,
  formatTime: formatTime,
  getNowTimeString: getNowTimeString,
}
