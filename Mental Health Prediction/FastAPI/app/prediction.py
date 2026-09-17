from model_loader import model
import pandas as pd 

def predict_mental_healh(req):
    input_data = {
        'Age': req.Age,
        'Gender': req.Gender, 
        'Country': req.Country, 
        'Academic_Level': req.Academic_Level, 
        'Most_Used_Platform': req.Most_Used_Platform, 
        'Purpose_Of_Use': req.Purpose_Of_Use, 
        'Avg_Daily_Usage_Hours': req.Avg_Daily_Usage_Hours,
        'Daily_Unlocks': req.Daily_Unlocks, 
        'Study_Hours': req.Study_Hours, 
        'Physical_Activity_Hours': req.Physical_Activity_Hours, 
        'Sleep_Hours_Per_Night': req.Sleep_Hours_Per_Night, 
        'Stress_Level': req.Stress_Level
    }

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)
    return prediction[0].item()
