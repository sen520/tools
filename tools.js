function createTable(table) {
  if (table.length < 1) {
    return '';
  }
  const result = [];
  result.push(`| ${table[0].map(() => '').join(' | ')} |`);
  result.push(`| ${table[0].map(() => ' --- ').join(' | ')} |`);
  for (const row of table) {
    result.push(`| ${row.join(' | ')} |`);
  }
  return result.join('\n');
}


var parse_number = /^-?\d+(?:\.\d*)?(?:e[+\-]?\d+)?$/i;
var isNumber = (num) => {
  return parse_number.test(num)
};


const moment = require('moment-timezone');
moment.tz(new Date(), 'Asia/Shanghai');

