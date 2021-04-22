import csv
import plotly_express as px 
import numpy as np 

def getDataSource(file_path):
    Coffee_in_ml = []
    sleep_in_hours = []

    with open(file_path) as file:
        df = csv.DictReader(file)
        for row in df:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
        print(sleep_in_hours)
    return {"x": Coffee_in_ml, "y":sleep_in_hours}

def find_correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation)
    print("Correlation between Coffee in ml and sleep in hours is ",correlation[1,0])

def setup():
    file_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(file_path)
    find_correlation(datasource)

setup()
