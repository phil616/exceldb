from .field import Field
class Controller:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Controller, cls).__new__(cls)
        return cls._instance
    def __init__(self,model:"Model") -> None:
        table_name = model.__name__
        table_dict = model.__dict__
        print("|table_name -> ",table_name)
        print("|table_dict -> ",table_dict)
    def register(self,database_name,table_name,table_dict):
        ...
    

class MetaClassConfig(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)
    def __init__(cls, name, bases, attrs):
        print("sb",cls.__subclasses__)
        if name == 'Model':
            return super().__init__(name, bases, attrs)
        else:
            Controller(cls)
            cls.mapping = {}
            for k, v in attrs.items():
                if isinstance(v, Field):
                    cls.mapping[k] = v
        print("mapping - > ",cls.mapping)
        super().__init__(name, bases, attrs)
class Model(dict, metaclass=MetaClassConfig):
    def __init__(self, **kwargs) -> None:
        print('Model __init__ called')
        print("kwargs -> ",kwargs)
        super().__init__(**kwargs)
        print("Model.__init__ called complete")

    def save(self):
        print("save called")
        print("self -> ",self)
        print("self.mapping -> ",self.mapping)

    @classmethod
    def create(cls, **kwargs):
        print("create called")
        print("kwargs -> ",kwargs)
        print("self.mapping -> ",cls.mapping)
        print("cls -> ",cls)

    def delete(self):
        print("delete called")
        print("self -> ",self)
        print("self.mapping -> ",self.mapping)

    def update(self, **kwargs):
        print("update called")
        print("kwargs -> ",kwargs)
        print("self.mapping -> ",self.mapping)
        print("self -> ",self)

    @classmethod
    def filter(cls, **kwargs):
        print("filter called")
        print("kwargs -> ",kwargs)
        print("self.mapping -> ",cls.mapping)
        print("cls -> ",cls)