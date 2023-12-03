# Dataflows


## Record

> DN1001

`Record` is a data structure that represents a single row of data. And `Record` is a `dict`-like object.

Every `Record` is a pydantic model

Attributes:
1. `id` : `int` - unique identifier of the record
2. `row` : `int` - row number in `Table` object
3. `data` : `pydantic model` - data of the record
4. `index` : `dict` - a mapping that key is int value that represents value's index in `data`.eg.{'1':name, '2':age}, for getitem and setitem



## Table

`Table` is a data structure that represents a table of data. And `Table` is a `list`-like object.

Attributes:
1. `name` : `str` - name of the table
2. `belongs_to` : `str` - name of the database that the table belongs to
3. `records` : `list` - list of `Record` objects

## Database
`database` is a data structure that represents a database. And every database represents a excel file

Attributes:
1. `name` : `str` - name of the database
2. `tables` : `list` - list of `Table` objects
3. `filepath` : `str` - path of the excel file


## WAL
`WAL` is a data structure that represents a write-ahead log. And every `WAL` represents a transaction.

Attributes:
1. `id` : `int` - unique identifier of the WAL
2. `record_time` : `datetime` - time of the record
3. `transaction_type` : `str` - type of the transaction,like INSERT,UPDATE,DELETE
4. `position` : `triple-tuple` - position of the record in the table,(database_name,table_name,row_number)
5. `old_value` : `Record` - old value of the record
6. `new_value` : `Record` - new value of the record


# Methods
init
