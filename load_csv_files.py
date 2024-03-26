import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin123@localhost:5433/road_accidents_db'
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv(fr'C:\Users\Kritika\OneDrive\Desktop\DA\Power BI Projects\Road Accident Analysis\road_accident.csv')
df.to_sql('road_accident' ,con = conn, if_exists='replace', index=False)