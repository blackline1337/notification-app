from typing import Optional, Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select, Depends

class Messages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str

engine = create_engine("mysql+mysqldb://dev:ops@localhost/message_data")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def main():
    
    SessionDep = Annotated[Session, Depends(get_session)]
    print(f"Session Object: {SessionDep}")


if __name__ =="__main__":
 main()