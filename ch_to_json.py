import json
import io

with io.open(project + '.json', 'w', encoding='utf-8') as fo:
    fo.write(unicode(json.dumps(data, ensure_ascii=False, indent=2, separators=(',', ': '))))