def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "Hello Rishi Chauhan!"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }
