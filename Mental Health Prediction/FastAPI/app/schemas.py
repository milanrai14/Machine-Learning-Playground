from pydantic import BaseModel
from typing import Literal

class HealthDetailRequest(BaseModel):
    Age: int 
    Gender: Literal['Male', 'Female']
    Country: str 
    Academic_Level : Literal['Undergraduate', 'Graduate', 'High School']
    Most_Used_Platform: str 
    Purpose_Of_Use: Literal['Networking', 'Education', 'Entertainment']
