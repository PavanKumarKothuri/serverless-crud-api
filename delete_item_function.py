import json

def lambda_handler(event, context):
    try:
        # Validate that queryStringParameters exists
        if 'queryStringParameters' not in event or event['queryStringParameters'] is None:
            raise ValueError("Query parameters are missing")
        
        # Extract the 'id' parameter
        item_id = event['queryStringParameters'].get('id')
        
        if not item_id:
            raise ValueError("The 'id' parameter is required")
        
        # Simulate deletion logic (e.g., from DynamoDB or other sources)
        # Uncomment the following if connected to DynamoDB:
        # dynamodb = boto3.resource('dynamodb')
        # table = dynamodb.Table('YourTableName')
        # table.delete_item(Key={'id': item_id})

        # Construct success response
        response = {"message": f"Item '{item_id}' deleted successfully"}
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    
    except ValueError as e:
        # Handle validation errors
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    
    except Exception as e:
        # Handle unexpected errors
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error", "details": str(e)})
        }
