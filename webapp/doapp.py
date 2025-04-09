import boto3
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


class MyModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client("s3", region_name="us-east-1")
        # s3.create_bucket(Bucket="mybucket")
        # s3.put_object(Bucket="mybucket", Key=self.name, Body=self.value, Config=config)
        s3.upload_file("coverage_bug.jpg", "mybucket", "s3_path.jpg")
        print("now_broken with thread patching")



def do_stuff(nr:int=5):
    Model.metadata.create_all(db.get_engine())
    spongebob = User(id=nr)
    # db.session.add_all([spongebob])
    #with app.app_context():
    md = MyModel("name", "value")
    print(md.name)
    db.session.add(spongebob)
    db.session.commit()
    md.save()
    print(spongebob.id)
    return spongebob

@app.route("/")
def hello_world():
    do_stuff()

    return "<p>Hello, World!</p>"