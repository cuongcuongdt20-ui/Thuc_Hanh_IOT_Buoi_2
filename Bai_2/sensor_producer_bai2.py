"""Bai 2: Mo phong cam bien gui du lieu JSON moi 3 giay."""

import json
import random

import pika

BROKER = "localhost"
PORT = 5672
USERNAME = "guest"
PASSWORD = "guest"
VHOST = "/"
QUEUE = "sensor_data_queue"
DEVICE_ID = "sensor01"
SEND_INTERVAL = 3


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
        print("Dang gui du lieu moi 3 giay - nhan Ctrl+C de dung", flush=True)

        while True:
            data = {
                "device_id": DEVICE_ID,
                "temperature": round(random.uniform(20, 40), 1),
                "humidity": round(random.uniform(30, 80), 1),
            }
            message = json.dumps(data)
            # Default exchange chuyen message den queue trung ten routing_key.
            channel.basic_publish(
                exchange="",
                routing_key=QUEUE,
                body=message.encode("utf-8"),
                properties=pika.BasicProperties(
                    content_type="application/json",
                    delivery_mode=2,
                ),
            )
            print("Da gui:", message, flush=True)
            # Van xu ly heartbeat cua RabbitMQ trong thoi gian cho.
            connection.sleep(SEND_INTERVAL)
    except KeyboardInterrupt:
        print("\nDa dung sensor producer")
    except pika.exceptions.AMQPError as error:
        print("Loi RabbitMQ:", error)
        print("Kiem tra broker va cau hinh ket noi o dau file.")
        raise SystemExit(1)
    finally:
        if connection is not None and connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
