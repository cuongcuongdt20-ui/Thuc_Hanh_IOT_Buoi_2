# Bai 1 - Consumer: lang nghe queue "iot_lab_queue" va in message nhan duoc
# Mo hinh: producer -> queue -> consumer
from datetime import datetime

import pika

BROKER = "localhost"        # dia chi RabbitMQ broker (cung broker voi producer)
PORT = 5672                 # cong AMQP mac dinh
USERNAME = "guest"          # tai khoan dang nhap broker
PASSWORD = "guest"          # mat khau
VHOST = "/"                 # virtual host tren broker
QUEUE = "iot_lab_queue"


# Ham nay duoc goi moi khi co message moi trong queue
def on_message(channel, method, properties, body):
    print("Da nhan message:", body.decode())
    print("Thoi gian nhan:", datetime.now().strftime("%H:%M:%S"))


# 1. Ket noi toi RabbitMQ broker
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=BROKER,
        port=PORT,
        virtual_host=VHOST,
        credentials=pika.PlainCredentials(USERNAME, PASSWORD),
    )
)
channel = connection.channel()

# 2. Tao queue (de consumer chay truoc producer van khong bi loi)
#    durable=True: queue duoc luu tren broker, khong mat khi broker khoi dong lai
#    (RabbitMQ 4.x bat buoc queue dung chung phai la durable)
channel.queue_declare(queue=QUEUE, durable=True)

# 3. Dang ky nhan message tu queue
#    auto_ack=True: nhan xong tu dong bao cho broker xoa message khoi queue
channel.basic_consume(queue=QUEUE, on_message_callback=on_message, auto_ack=True)

# 4. Chay lien tuc cho toi khi nhan Ctrl+C
print("Dang cho message tu queue", QUEUE, "- nhan Ctrl+C de dung")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Da dung consumer")

connection.close()
