from typing import Optional, Generator
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Messages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str

engine = create_engine("mysql+pymysql://dev:ops@localhost/message_data")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

def main():
    create_db_and_tables()
    with Session(engine) as session:
        new_msg = Messages(message="Hello world!")
        session.add(new_msg)
        session.commit()
        print("Message Added!")


if __name__ =="__main__":
 main()