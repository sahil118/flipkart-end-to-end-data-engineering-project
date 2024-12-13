import http.client
import json
import os
import boto3
from datetime import datetime


def lambda_handler(event, context):
    api_key = os.environ.get('RAPIDAPI_KEY')  
    api_host = os.environ.get('RAPIDAPI_HOST')
    conn = http.client.HTTPSConnection("real-time-flipkart-api.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': api_host
    }

    conn.request("GET", "/products-by-brand?brand_id=tyy%2C4io&page=1&sort_by=popularity", headers=headers)

    res = conn.getresponse()
    data = res.read()

    decoded_data = data.decode("utf-8")
    parsed_data = json.loads(decoded_data) 

    client = boto3.client('s3')
    filename = "flipkart_raw_" + str(datetime.now()) +  ".json"
    client.put_object(
        Bucket = "flipkart-data-project-sahil",
        Key="flip-raw-data/pending-raw-data/" + filename,
        Body = json.dumps(parsed_data)
    )
   
