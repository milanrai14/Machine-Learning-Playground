from pydantic import BaseModel
from typing import Literal

class HealthDetailRequest(BaseModel):
    Age: int 
    Gender: Literal['Male', 'Female']
    Country: str 
    Academic_Level : Literal['Undergraduate', 'Graduate', 'High School']
    Most_Used_Platform: str 
    Purpose_Of_Use: Literal['Networking', 'Education', 'Entertainment']
    Avg_Daily_Usage_Hours: float
    Daily_Unlocks: int 
    Study_Hours: float
    Physical_Activity_Hours: float
    Sleep_Hours_Per_Night: float
    Stress_Level: str
    

    


