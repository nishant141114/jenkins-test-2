def lambda_handler(event, context):

    print("I am second test")
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }