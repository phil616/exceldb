from typing import List, Dict, Any, Optional, Union, Tuple,Literal
from datastructures import Record
from datetime import datetime
class Transaction(dict):
    def __init__(self,
                 id:Optional[int],
                 transaction_type:Literal["UPDATE","CREATE","DELETE"],
                 position:Optional[Tuple[str,str,int]],
                 old_value:Optional[Record],
                    new_value:Optional[Record],
                 ) -> None:
        if id is None:
            self.id = None # generate id by random
        self.record_time = datetime.now()
        self.transaction_type = transaction_type
        self.position = position
        self.old_value = old_value
        self.new_value = new_value
        if transaction_type == "UPDATE":
            assert self.old_value is not None
            assert self.new_value is not None
        elif transaction_type == "CREATE":
            assert self.new_value is not None
        elif transaction_type == "DELETE":
            assert self.old_value is not None
        super().__init__(id=id,
                         record_time=self.record_time,
                         transaction_type=self.transaction_type,
                         position=self.position,
                         old_value=self.old_value,
                         new_value=self.new_value)
        
    def __get__(self, instance, owner):
        return self
    def __repr__(self) -> str:
        return f"Transaction({self.id},{self.transaction_type},{self.position},{self.old_value},{self.new_value})"
