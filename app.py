from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://project-db:root@34.89.124.0/projectdb'
db=SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)