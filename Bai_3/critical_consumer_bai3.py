import pika

HOST = "localhost"

EXCHANGE_NAME = "iot_alert_exchange"
QUEUE_NAME = "critical_queue"
ROUTING_KEY = "critical"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST)
)

channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type="direct",
    durable=True
)

channel.queue_declare(
    queue=QUEUE_NAME,
    durable=True
)

channel.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=QUEUE_NAME,
    routing_key=ROUTING_KEY
)


def callback(ch, method, properties, body):
    message = body.decode("utf-8")
    print(f"[critical_queue] Da nhan: {message}")


channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=callback,
    auto_ack=True
)

print("Critical Consumer dang cho message...")

try:
    channel.start_consuming()

except KeyboardInterrupt:
    print("\nDung Critical Consumer")
    connection.close()