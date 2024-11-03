import json

# Function to handle the subscription logic
def handle_subscription(user_id):
    # Example logic for handling subscription
    data = {
        "user_id": user_id,
        "subscribed": True
    }
    with open('subscriptions.json', 'w') as f:
        json.dump(data, f)
    return "Subscription successful."
