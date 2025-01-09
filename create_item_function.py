import json
    
def lambda_handler(event, context):
        body = json.loads(event['body'])
        item = body.get('item')
        response = {"message": f"Item '{item}' created successfully"}
        return {
            "statusCode": 201,
            "body": json.dumps(response)
        }    