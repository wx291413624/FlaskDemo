from flask_sqlalchemy import SQLAlchemy

from .. import app

# sudo  sqlacodegen mysql://root:Kiretyo1521@47.95.235.183:3306/guns  --outfile ms.py
db = SQLAlchemy(app)
