// = 后面是一个函数
const formatNumber = (n) => {
  n = n.toString();
  return n[1] ? n : '0' + n;
}

/**
 * 日期格式化
 * @param date 日期
 * @param format 格式，例如：Y-M-D h:m:s, Y年-M月-D日
 */
function formateDate(date, format) {
  var formatArr = ['Y', 'M', 'D', 'h', 'm', 's']
  var returnArr = [];

  returnArr.push(date.getFullYear());
  returnArr.push(formatNumber(date.getMonth() + 1));
  returnArr.push(formatNumber(date.getDate()));
  returnArr.push(formatNumber(date.getHours()));
  returnArr.push(formatNumber(date.getMinutes()));
  returnArr.push(formatNumber(date.getSeconds()));

  for(var i in returnArr){
    // 把format格式里面的Y M D h m s替换成相应的日期
    format = format.replace(formatArr[i], returnArr[i])
  }
  return format
}

/**
 * 获取星期几，返回中文
 * @param date 日期
 */
function getWeekday(date) {
  var wd = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五'];
  var day = date.getDay();
  return wd[day];
}

module.exports = {
  formateDate: formateDate,
  getWeekday: getWeekday
}