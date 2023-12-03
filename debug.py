from exceldb import meta
from exceldb import field
class User(meta.Model):
    username = field.CharField(max_length=50)
    password = field.CharField(max_length=50)
    __filename__ = 'user.xlsx'
    __tablename__ = 'user'
    __abstract__ = False

User.filter(username='admin')