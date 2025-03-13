from flask import Flask
from flask_sqlalchemy_lite import SQLAlchemy
from flask_sqlalchemy_lite._extension import _close_async_sessions
from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



# engine = create_engine("sqlite://", echo=True)

class Model(DeclarativeBase):
    pass

class User(Model):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)


app = Flask(__name__)
app.debug = True
app.testing = True
app.config |= {
    "SQLALCHEMY_ENGINES": {
        "default": "sqlite://",
    },
}

db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    pass
#    Model.metadata.create_all(db.get_engine())
#    do_stuff()


# app.teardown_appcontext_funcs.remove(_close_async_sessions)


def do_stuff(nr:int=5):
    Model.metadata.create_all(db.get_engine())
    spongebob = User(id=nr)
    # db.session.add_all([spongebob])
    #with app.app_context():
    db.session.add(spongebob)
    db.session.commit()
    print(spongebob.id)
    return spongebob

@app.route("/")
def hello_world():
    do_stuff()

    return "<p>Hello, World!</p>"