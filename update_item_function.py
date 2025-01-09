import json

def lambda_handler(event, context):
    try:
        # Ensure 'body' exists in the event
        if 'body' not in event:
            raise ValueError("Request body is missing")
        
        # Parse the JSON body
        body = json.loads(event['body'])
        item_id = body.get('id')
        updated_data = body.get('data')

        # Validate required fields
        if not item_id or not updated_data:
            raise ValueError("Both 'id' and 'data' fields are required")
        
        # Construct the response
        response = {"message": f"Item '{item_id}' updated with data: {updated_data}"}
        
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
