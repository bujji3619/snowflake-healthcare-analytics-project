import pandas as pd
import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    obj = s3.get_object(
        Bucket='healthcare-raw-data-bucket-12345',
        Key='healthcare_data.csv'
    )

    df = pd.read_csv(obj['Body'])

    df['treatment_cost'] = df['treatment_cost'] * 1.10

    df.to_csv('/tmp/processed.csv', index=False)

    s3.upload_file(
        '/tmp/processed.csv',
        'healthcare-processed-data-bucket-12345',
        'processed_healthcare.csv'
    )