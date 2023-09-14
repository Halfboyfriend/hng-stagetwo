import json

def handler(event, context):
    # Your Flask app code goes here
    from ..api import app  # Import your Flask app
    with app.app_context():
        response = app.test_client().get('/api/hello')  # Replace with your route
        return {
            "statusCode": 200,
            "body": json.dumps(response.json)
        }
