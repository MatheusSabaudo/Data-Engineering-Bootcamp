import uuid
import json
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(producer_config)

# Callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def take_order():
    user = input("Name of the user: ")
    item = input("Name of the item: ")
    quantity = int(input("Quantity: "))

    # Order data to be sent to Kafka
    order = { 
        'order_id': str(uuid.uuid4()), # Generate a unique order ID
        'user': user,
        'item': item,
        'quantity': quantity
    }

    return order

#Get order from user input
order = take_order()

value = json.dumps(order).encode('utf-8') # Serialize the order data to JSON and encode it to bytes

producer.produce(
    topic='orders', 
    value=value,
    callback=delivery_report
) 

producer.flush() # Ensure all messages are sent before exiting

print(f"Produced order: {order}")