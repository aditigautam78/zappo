from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

db = SQLAlchemy()
Base = automap_base()