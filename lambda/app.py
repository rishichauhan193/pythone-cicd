def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "Hello Aryan!"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }
