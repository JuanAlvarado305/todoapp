# Import BaseModel from pydantic library for data validation and schema definition
from pydantic import BaseModel
# Import several components from sqlmodel library for ORM functionality
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str = Field(default="")
    isComplete: bool = Field(default=False)
    user_id: int = Field(default=None, foreign_key="user.id")

class User(SQLModel, table=True):
    password: str = Field(default=None)
    email: str = Field(default="")
    id: int | None = Field(default=None, primary_key=True)


# Define database name
mysql_name = "test_db"
# Construct MySQL connection URL using PyMySQL driver
# Format: mysql+pymysql://username:password@host:port/database_name
mysql_url = f"mysql+pymysql://root:password@localhost:3306/{mysql_name}"
# Create database engine using the connection URL
# This establishes a connection pool to the database
engine = create_engine(mysql_url)

# Function to create database tables based on SQLModel definitions
def create_db_and_tables():
    # This will create all tables that don't exist yet based on the SQLModel metadata
    SQLModel.metadata.create_all(engine)

# Function to provide a database session context
def get_session():
    # Create a new session using the engine
    with Session(engine) as session:
        # Yield the session to the caller
        # This allows the session to be used as a context manager or dependency
        yield session