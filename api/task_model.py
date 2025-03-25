from pydantic import BaseModel  # Imports BaseModel from pydantic for data validation

cur_id = 0  # Global counter for task IDs

# Function to increment and return the current ID
def increment():
    global cur_id
    cur_id += 1
    return cur_id

# Task model class
class Task(BaseModel):
    id: int
    description: str = ""  # Default empty string
    isComplete: bool = False  # Default False

    # Custom constructor that automatically assigns a new ID
    def __init__(self, **data):
        super().__init__(id=increment(), **data)