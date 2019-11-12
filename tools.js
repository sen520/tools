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


const is_array = (value) => {
  return value &&
    typeof value === 'object' &&
    typeof value.length === 'number' &&
    typeof value.splice === 'function' &&
    !(value.propertyIsEnumerable('length'));
};