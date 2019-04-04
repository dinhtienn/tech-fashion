import mongoengine

# mongodb://project:techmarket12@ds111063.mlab.com:11063/c4e20-project

host = "ds111063.mlab.com"
port = 11063
db_name = "c4e20-project"
user_name = "project"
password = "techmarket12"

def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )