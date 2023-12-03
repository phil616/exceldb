import openpyxl as xl
import os
from typing import List,Optional,Union,Sequence
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class Record():
    def __init__(self,
                 row:int, 
                 data:dict,
                 index:dict,
                 id:Optional[int] = None,
                 ):
        # more for DN1001
        self.row = row
        self.data = data
        self.index = index
        self.id = id
    def __str__(self) -> str:
        return f"ExcelDB Record({self.id}) at row {self.row}"
    def __get__(self, instance, owner):
        return self.data
    def __getitem__(self, key):
        # TODO raise KeyError if not found
        # user may use record[0] to get the record elem by index
        # user may also use record['0'] to get the record elem by name
        if isinstance(key, int):
            self.data[self.index[key]]
        elif isinstance(key, str):
            return self.data[key]
        else:
            raise NotImplementedError("Only support int and str as key")
class Table():
    def __init__(self,
                 name:str,
                 records:List[Record],
                 belongs_to:Optional[str] = None,
    ) -> None:
        self.name = name
        self.records = records
        self.belongs_to = belongs_to
    def __str__(self) -> str:
        return f"ExcelDB Table({self.name})"


class Database():
    def __init__(
            self,
            name:str,
            tables:List[Table],
            belongs_to:Optional[str] = None,
    ):
        self.name = name
        self.tables = tables
        self.belongs_to = belongs_to
    def __str__(self) -> str:
        return f"ExcelDB Database({self.name})"

