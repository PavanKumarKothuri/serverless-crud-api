import json
    
def lambda_handler(event, context):
    item_id = event['queryStringParameters'].get('id')
    response = {"message": f"Details of item '{item_id}'"}
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }