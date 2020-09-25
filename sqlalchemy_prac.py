import os
import sqlalchemy
from sqlalchemy import create_engine,text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engineDb = create_engine(os.environ['DATABASE_URL'])
Base = declarative_base()
sessionDb = sessionmaker()
sessionDb.configure(bind=engineDb)

class User(Base):
    __tablename__= 'users'
    id = Column(Integer, Sequence('user_id_seq'),primary_key =True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User (name={}, fullname={} , nickname={})>".format(self.name, self.fullname, self.nickname)

if __name__ == '__main__':
    # print(sqlalchemy.__version__)
    # user = User(name = "Consuela", fullname='Princess Consuela Banahammock', nickname='PCB')
    # Base.metadata.drop_all(engineDb)
    # Base.metadata.create_all(engineDb)
    sessionObj = sessionDb()
    for i in sessionObj.query(User).from_statement(text('select * from users where id < 26')).all():
        print(i.name)
    sessionObj.delete(User)
    sessionObj.close()