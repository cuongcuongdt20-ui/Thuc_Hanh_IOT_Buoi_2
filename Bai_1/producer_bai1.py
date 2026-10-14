# Bai 1 - Producer: gui message vao queue "iot_lab_queue"
# Mo hinh: producer -> queue -> consumer
import pika

BROKER = "localhost"        # dia chi RabbitMQ broker
PORT = 5672                 # cong AMQP mac dinh
USERNAME = "guest"          # tai khoan dang nhap broker
PASSWORD = "guest"          # mat khau
VHOST = "/"                 # virtual host tren broker
QUEUE = "iot_lab_queue"

HO_TEN = "Nguyen Duy Cuong"
MA_SV = "B23DCCN112"

message = f"Xin chao tu ung dung Python AMQP - {MA_SV} - {HO_TEN}"

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

# 2. Tao queue (neu queue da ton tai thi dung lai queue do)
#    durable=True: queue duoc luu tren broker, khong mat khi broker khoi dong lai
#    (RabbitMQ 4.x bat buoc queue dung chung phai la durable)
channel.queue_declare(queue=QUEUE, durable=True)

# 3. Gui message vao queue
#    exchange="" la default exchange: message duoc dua thang vao queue
#    co ten trung voi routing_key
channel.basic_publish(exchange="", routing_key=QUEUE, body=message)

print("Da gui message:", message)

# 4. Dong ket noi
connection.close()
