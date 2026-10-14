import pika

HOST = "localhost"
EXCHANGE_NAME = "iot_alert_exchange"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST)
)

channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type="direct",
    durable=True
)

alerts = [
    (
        "info",
        "He thong dang hoat dong binh thuong"
    ),
    (
        "warning",
        "Nhiet do phong may vuot nguong warning"
    ),
    (
        "critical",
        "Cam bien kho lanh mat ket noi critical"
    )
]

for routing_key, message in alerts:

    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=routing_key,
        body=message
    )

    print(f"Da gui [{routing_key}]: {message}")

connection.close()