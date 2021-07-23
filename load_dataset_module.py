#importing necessary libraries
import csv

# opening the csv file 
file = open('activity_context_tracking_data.csv', mode='r', encoding='utf8')
file_dict = csv.DictReader(file)  # We parsed this as a csv data file


def Activity_Data():
    'returns the activity data dictionary'
    activity_data = {}  # here we initialize an empty dictionary that will contain the activity_data
    # sample_dict = {
    # name = "George",
    # country = "UK"
    # 0 = ["orX","orY",	"orZ",..]
    #   
    # }
    for rows in file_dict:
        activity_data[rows['_id']] = [int(rows['orX']), int(rows['orY']),int(rows['orZ']),float(rows['rX']),float(rows['rY']),float(rows['rZ']),float(rows['accX']),float(rows['accY']),float(rows['accZ']),
        float(rows['gX']),float(rows['gY']),float(rows['gZ']),float(rows['orX']),float(rows['mX']),float(rows['mY']),float(rows['mZ']),rows['activity']]
    return activity_data

def Activity_Features():
    'returns the computed features from the activity data'
    activity_features = {}
    for rows in file_dict:
        activity_features[rows['_id']] = {}
    return activity_features
