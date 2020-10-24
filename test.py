from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() 
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://edkngdec:b1hq_EAX-fAcPJsEA8kyP9Pp32ZPUWkT@kandula.db.elephantsql.com:5432/edkngdec" 

db.init_app(app) 


@app.route('/')
def hello_world():
  sql_cmd="""select * from users""" 
  query_data=db.engine.execute(sql_cmd).fetchall()
  print(query_data) 
  return 'Hello World' 

if __name__=='__main__':
  app.run() 

