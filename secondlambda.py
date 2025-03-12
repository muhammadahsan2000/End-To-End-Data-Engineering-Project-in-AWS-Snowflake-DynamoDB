#this function get data from dynomodb and load s3 
from datetime import datetime
import pandas as pd
import boto3
from io import StringIO

def handle_insert(record):
    print("Handling Insert: ", record)
    data_dict = {}  # ✅ Changed variable name from dict to avoid conflicts with Python's built-in dict

    for key, value in record['dynamodb']['NewImage'].items():
        for dt, col in value.items():
            data_dict.update({key: col})

    dff = pd.DataFrame([data_dict])
    return dff

def lambda_handler(event, context):
    print(event)
    df = pd.DataFrame()
    dff = None  # ✅ Initialize dff before using it

    for record in event['Records']:
        table = record['eventSourceARN'].split("/")[1]

        if record['eventName'] == "INSERT": 
            dff = handle_insert(record)

    # ✅ Check if dff is assigned before using it
    if dff is not None:
        df = dff

    if not df.empty:
        all_columns = list(df)
        df[all_columns] = df[all_columns].astype(str)

        path = table + "_" + str(datetime.now()) + ".csv"
        print(event)

        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        s3 = boto3.client('s3')
        bucketName = "de-proj-weatherdata".strip()  # ✅ Remove extra space
        key = "snowflake/" + table + "_" + str(datetime.now()) + ".csv"
        print(key)
        
        s3.put_object(Bucket=bucketName, Key=key, Body=csv_buffer.getvalue())

    print('Successfully processed %s records.' % str(len(event['Records'])))
