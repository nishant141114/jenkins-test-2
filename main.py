def lambda_handler(event, context):
    print("In lambda_handler")
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }