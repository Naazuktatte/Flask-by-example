import os
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engineDb = create_engine(os.environ['DATABASE_URL'], echo=True)
Base = declarative_base()
sessionDb = sessionmaker()
sessionDb.configure(bind=engineDb)

class User(Base):
    __tablename__= 'users'
    id = Column(Integer, Sequence('user_id_seq'),primary_key =True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    # def __init__(self, id, name, fullname , nickname):
    #     self.id = id
    #     self.name = name
    #     self.fullname = fullname
    #     self.nickname = nickname

    def __repr__(self):
        return "<User (name={}, fullname={} , nickname={})>".format(self.name, self.fullname, self.nickname)

if __name__ == '__main__':
    # print(sqlalchemy.__version__)
    user = User(name = "Consuela", fullname='Princess Consuela Banahammock', nickname='PCB')
    Base.metadata.drop_all(engineDb)
    Base.metadata.create_all(engineDb)
    sessionObj = sessionDb()
    sessionObj.add(user)
    sessionObj.add_all([
                        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
                        User(name='mary', fullname='Mary Contrary', nickname='mary'),
                        User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
    sessionObj.commit()
    our_user = sessionObj.query(User)
    print('>>>>>>>our_user: ', our_user)