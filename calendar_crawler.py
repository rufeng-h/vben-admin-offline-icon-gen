import csv
import io
from pathlib import Path
from typing import Optional, Literal, List

import requests
import pandas as pd
from pydantic import BaseModel, ConfigDict, TypeAdapter, Field
from pydantic.alias_generators import to_camel


class CanlendarItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    avoid: str
    chinese_zodiac: str
    constellation: str
    cdate: str = Field(alias='date')
    lunar_calendar: str
    solar_terms: str
    suit: Optional[str] = None
    type: int
    type_des: str
    year_tips: str


class CalendarCrawler:
    def __init__(self):
        self._session = requests.session()
        self._app_id = "fwvespfpkrfbsiom"
        self._app_secret = "ek9zbWNYRmhFdVcxcWErZWVmWCtwdz09"

    def get_year_calendar(self, _from, _to: int = None, _format: Literal['csv', 'json'] = 'csv') -> str:

        if _to is None:
            _to = _from + 1

        params = {
            'app_id': self._app_id,
            'app_secret': self._app_secret
        }
        items = []
        for i in range(_from, _to):
            response = requests.get("https://www.mxnzp.com/api/holiday/list/year/{}".format(i), params=params)
            for data in response.json()['data']:
                for day in data['days']:
                    print(day)
                    items.append(CanlendarItem(**day))

        if _format == 'json':
            return TypeAdapter(List[CanlendarItem]).dump_json(items).decode()
        elif _format == 'csv':
            data = TypeAdapter(List[CanlendarItem]).dump_python(items)
            df = pd.DataFrame(data=data)
            strio = io.StringIO()
            df.to_csv(strio, quoting=csv.QUOTE_NONNUMERIC, index=False, lineterminator='\n')
            return strio.getvalue()

        raise ValueError(f'不支持的格式：{_format}')


if __name__ == '__main__':
    crawler = CalendarCrawler()
    result = crawler.get_year_calendar(2024)
    Path('./2024.csv').write_text(result, encoding='utf-8')
