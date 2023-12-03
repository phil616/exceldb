import threading
import collections
import threading
from engine import Transaction
from queue import Queue
from openpyxl import load_workbook
class ThreadSafeSet:
    def __init__(self):
        self.lock = threading.Lock()
        self.set = collections.OrderedDict()

    def add(self, item):
        try:
            self.set[item]
        except KeyError:
            with self.lock:
                self.set[item] = None
                return
        raise KeyError(f"{item} already exists")
    def pop(self):
        with self.lock:
            if len(self.set) == 0:
                return None
            item = next(iter(self.set))
            del self.set[item]
            return item
        
class CommunicationProxy:
    """the user interface of the background thread"""
    WAL = Queue()
    def add_transaction(self,transaction:Transaction):
        self.WAL.put(transaction)
    def get_transaction(self) -> Transaction:
        yield self.WAL.get()
class Connection:
    def __call__(self,file,cp:CommunicationProxy,*args, **kwargs):
        wb = load_workbook(file)
        for transaction in cp.WAL:
            print("transaction -> ",transaction)
    ...


class DispatchFactory:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DispatchFactory, cls).__new__(cls)
        return cls._instance
    

    def __call__(self, database,*args, **kwargs):
        databases = ThreadSafeSet()
        try:
            databases.add(database)
            cp = CommunicationProxy()
            threading.Thread(target=Connection, args=(database,cp,),daemon=True).start()
            return cp
        except KeyError:
