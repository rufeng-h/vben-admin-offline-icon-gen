from pathlib import Path

import dmPython

conn = dmPython.connect(user='SYSDBA', password='1234567890.', server='localhost', port=5238)
cursor = conn.cursor()
cursor.execute("select date from calendar where type = '1' or type = '2' and date >= '2018-01-01'")
values = cursor.fetchall()
# print(values)
cursor.close()
conn.close()

# with open("./workday.txt", 'w') as f:
#     for d in values:
#         f.write(d[0].strftime('%Y-%m-%d') + "\n")
# import json
import time
# from pathlib import Path

import requests

# params = {
#     "app_id": "fwvespfpkrfbsiom",
#     "app_secret": "ek9zbWNYRmhFdVcxcWErZWVmWCtwdz09",
# }
#
# for i in range(2002, 2024):
#     response = requests.get("https://www.mxnzp.com/api/holiday/list/year/{}".format(i), params=params)
#     print(response.json())
#     Path(f'./data/{i}.json').write_text(json.dumps(response.json()['data'], ensure_ascii=False, indent=4),
#                                         encoding='utf-8')
#     time.sleep(2)


# records = []
# for i in range(2002, 2024):
#     text = Path(f'./data/{i}.json').read_text(encoding='utf-8')
#     data = json.loads(text)
#     for d in map(lambda x: x['days'], data):
#         records.extend(d)
# Path('./calendar.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')

print(Path('./workday.txt').read_text(encoding='utf-8').split())