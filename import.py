import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("Database url is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY,username VARCHAR NOT NULL,password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE book_review (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL,rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE myTable(isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    f=open("books.csv")
    reader=csv.reader(f)
    for isbn,tit,auth,yr in reader:
        if yr=="year":
            print("skipped first line")
        else:
            db.execute("INSERT INTO myTable (ISBN,TITLE,AUTHOR,YEAR) VALUES (:ISBN,:TITLE,:AUTHOR,:YEAR)",{"ISBN":isbn, "TITLE":tit, "AUTHOR":auth, "YEAR":yr})
    print("done")
    db.commit()
if __name__=="__main__":
    main()
