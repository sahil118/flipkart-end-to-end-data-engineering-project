import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd 

def product(data):
    product_list = []
    for row in data['products']:
        product_id = row['pid']
        Brand_Name = row['brand']
        Product_name = row['title']
        link = row['url']
        badge = row['badge']
        Mrp_price = row['mrp']
        Actuall_price = row['price']
        Product_fetures = row['highlights']
        product_element = {'product_id':product_id,'Brand_Name':Brand_Name,'Product_name':Product_name,
                        'link':link,'badge':badge,'Mrp_price':Mrp_price,'Selling_price':Actuall_price,'Fetures':Product_fetures}
        product_list.append(product_element)
    
    return product_list

def rating(data):
    
    rating_list = []
    for row in data['products']:
        product_id = row['pid']
        Average_review = row['rating']['average']
        total_ratings = row['rating']['count']
        Review_count = row['rating']['reviewCount']
        # Breaking down the 'breakup' list into individual star ratings
        one_star = row['rating']['breakup'][0]  # Number of 1-star ratings
        two_star = row['rating']['breakup'][1]  # Number of 2-star ratings
        three_star = row['rating']['breakup'][2]  # Number of 3-star ratings
        four_star = row['rating']['breakup'][3]  # Number of 4-star ratings
        five_star = row['rating']['breakup'][4]  # Number of 5-star ratings
        rating_elements = {'Average_review':Average_review,'total_ratings':total_ratings,
                        'Feed_back':Review_count,'one_star':one_star,'two_star':two_star,
                        'three_star':three_star,'four_star':four_star,'five_star':five_star,'product_id':product_id}
        rating_list.append(rating_elements)
    
    return rating_list

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucket = "flipkart-data-project-sahil"
    Key = "flip-raw-data/pending-raw-data/"


    flipkart_data = []
    flipkart_keys = []
    for file in s3.list_objects(Bucket=Bucket,Prefix=Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1] == "json":
            response = s3.get_object(Bucket=Bucket,Key=file_key)
            content = response['Body']
            jsonObject = json.loads(content.read())
            flipkart_data.append(jsonObject)
            flipkart_keys.append(file_key)
    

    for data in flipkart_data:
        product_list = product(data)
        rating_list =  rating(data)

        prd_df = pd.DataFrame.from_dict(product_list)
        prd_df = prd_df.drop_duplicates(subset=['product_id'])

        rating_df = pd.DataFrame.from_dict(rating_list)
        rating_df = rating_df.drop_duplicates(subset=['product_id'])

        product_key = "flip-trans-data/product-details-data/product_transformed_data" + str(datetime.now()) + ".csv"
        product_buffer = StringIO()
        prd_df.to_csv(product_buffer,index=False)
        prd_content = product_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=product_key, Body=prd_content)

        rating_key = "flip-trans-data/rating-details-data/rating_transformed_data" + str(datetime.now()) + ".csv"
        rating_buffer = StringIO()
        rating_df.to_csv(rating_buffer,index=False)
        rating_content = rating_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=rating_key, Body=rating_content)
    

    s3_resource = boto3.resource('s3')
    for key in flipkart_keys:
        copy_source = {
            'Bucket' : Bucket,
            'Key' : key
        }
        s3_resource.meta.client.copy(copy_source,Bucket,"flip-raw-data/processed-raw-data/" + key.split("/")[-1])
        s3_resource.Object(Bucket,key).delete()




