"""Bai 2: Nhan du lieu cam bien va hien thi canh bao."""

import json
import math

import pika

BROKER = "localhost"
PORT = 5672
USERNAME = "guest"
PASSWORD = "guest"
VHOST = "/"
QUEUE = "sensor_data_queue"


def on_message(channel, method, properties, body):
    try:
        data = json.loads(body.decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Payload phai la JSON object")
        device_id = data["device_id"]
        temperature = data["temperature"]
        humidity = data["humidity"]
        if not isinstance(device_id, str) or not device_id.strip():
            raise ValueError("device_id phai la chuoi khong rong")
        for value in (temperature, humidity):
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError("Nhiet do va do am phai la so huu han")
    except (ValueError, KeyError, UnicodeDecodeError) as error:
        print("Bo qua message khong hop le:", error, flush=True)
        # Khong dua message loi tro lai queue de tranh lap vo han.
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        return

    print("Device:", device_id)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    if temperature > 35:
        print("CANH BAO: Nhiet do cao")
    if humidity < 40:
        print("CANH BAO: Do am thap")
    print("-" * 40, flush=True)
    # Chi xac nhan sau khi da xu ly du lieu.
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = None
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=BROKER,
                port=PORT,
                virtual_host=VHOST,
                credentials=pika.PlainCredentials(USERNAME, PASSWORD),
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue=QUEUE, on_message_callback=on_message, auto_ack=False
        )
        print("Dang cho du lieu tu", QUEUE, "- nhan Ctrl+C de dung", flush=True)
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nDa dung monitoring consumer")
    except pika.exceptions.AMQPError as error:
        print("Loi RabbitMQ:", error)
        print("Kiem tra broker va cau hinh ket noi o dau file.")
        raise SystemExit(1)
    finally:
        if connection is not None and connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
