def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "welcome Aryan!"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }
