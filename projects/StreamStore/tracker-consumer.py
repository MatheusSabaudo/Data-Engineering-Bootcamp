import json
from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092', # Kafka broker address
    'group.id': 'order-tracker', # Unique group ID for the consumer
    'auto.offset.reset': 'earliest' # Start consuming from the earliest message if no offset is found
}

consumer = Consumer(consumer_config)

consumer.subscribe(['orders']) # Subscribe to the 'orders' topic
print("Tracking orders...")

try:

    while True:
        msg = consumer.poll(1.0) # Poll for messages with a timeout of 1 second

        if msg is None:
            continue # No message received, continue polling
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue # Handle any errors that occur during consumption
        
        value = msg.value().decode('utf-8') # Decode the message value from bytes to string
        order = json.loads(value) # Parse the JSON string to a Python dictionary
        print(f"Received order: {order['quantity']} x {order['item']} for user {order['user']} (Order ID: {order['order_id']})")

except KeyboardInterrupt:
    print("Stopping order tracker...")
    
finally:
    consumer.close()