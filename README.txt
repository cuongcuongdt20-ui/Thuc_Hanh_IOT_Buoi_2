THỰC HÀNH IOT BUỔI 2: LẬP TRÌNH PYTHON VỚI GIAO THỨC AMQP


__________BAI1_____________
Sinh viên: Nguyen Duy Cuong
Mã sinh viên: B23DCCN112


1. BROKER SỬ DỤNG

- Broker: RabbitMQ 4.3.6 (Erlang/OTP 27) cài trên máy cá nhân
- Địa chỉ: localhost
- Cổng: 5672 (cổng AMQP mặc định)
- Tài khoản: guest / guest (tài khoản mặc định của RabbitMQ)
- Thư viện Python: pika

Nếu dùng broker khác, sửa các biến BROKER, PORT, USERNAME, PASSWORD, VHOST ở đầu mỗi file .py.

2. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH

Chuẩn bị (làm một lần):
- Cài Python 3.x và bật RabbitMQ.
- Cài thư viện:
    pip install pika
- Trên Windows, nếu lệnh "python" báo "Python was not found" thì thay
  bằng "py", ví dụ: py consumer_bai1.py
Các bước chạy:

Bước 1: mở terminal thứ nhất, chạy consumer:
    cd Bai_1
    python consumer_bai1.py
  Chương trình chờ message từ queue iot_lab_queue, nhấn Ctrl+C để dừng.

Bước 2: mở terminal thứ hai, chạy producer:
    cd Bai_1
    python producer_bai1.py
  Mỗi lần chạy gửi một message vào queue iot_lab_queue rồi kết thúc.

Ghi chú: có thể chạy producer trước. Message được giữ trong queue
và consumer sẽ nhận khi được bật lên.


3. KẾT QUẢ ĐẠT ĐƯỢC

- producer_bai1.py kết nối được tới broker, tạo queue iot_lab_queue
  và gửi message gồm lời chào, mã sinh viên, họ tên.
- consumer_bai1.py kết nối cùng broker, lắng nghe queue iot_lab_queue,
  in ra nội dung message và thời điểm nhận.

Màn hình producer:
    Da gui message: Xin chao tu ung dung Python AMQP - B23DCCN112 - Nguyen Duy Cuong

Màn hình consumer:
    Dang cho message tu queue iot_lab_queue - nhan Ctrl+C de dung
    Da nhan message: Xin chao tu ung dung Python AMQP - B23DCCN112 - Nguyen Duy Cuong
    Thoi gian nhan: 10:21:57


__________BAI3_____________
BÀI 3 - MÔ PHỎNG HỆ THỐNG ĐIỀU PHỐI CẢNH BÁO IOT VỚI EXCHANGE

1. MỤC TIÊU

- Làm quen với exchange và routing key trong AMQP
- Sử dụng direct exchange để phân phối cảnh báo theo mức độ

2. BROKER SỬ DỤNG

- Broker: RabbitMQ 4.3.6 (Erlang/OTP 28.5.0.7)
- Địa chỉ: localhost
- Cổng: 5672 (cổng AMQP mặc định)
- Tài khoản: guest / guest
- Thư viện Python: pika

3. CÁC THÀNH PHẦN

- Exchange: iot_alert_exchange
- Exchange type: direct
- Routing key: info, warning, critical
- Queue: warning_queue bind với routing key warning
- Queue: critical_queue bind với routing key critical

Các file:
- Bai_3/alert_producer_bai3.py
- Bai_3/warning_consumer_bai3.py
- Bai_3/critical_consumer_bai3.py

4. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH

Chuẩn bị (làm một lần):
- Cài Python 3.x.
- Đảm bảo RabbitMQ đang chạy
- Cài thư viện:
    pip install pika

Các bước chạy (mỗi terminal bắt đầu tại thư mục gốc project):

Bước 1: mở terminal thứ nhất, chạy warning consumer:
    cd Bai_3
    python warning_consumer_bai3.py

Bước 2: mở terminal thứ hai, chạy critical consumer:
    cd Bai_3
    python critical_consumer_bai3.py

Bước 3: mở terminal thứ ba, chạy producer:
    cd Bai_3
    python alert_producer_bai3.py

5. KẾT QUẢ ĐẠT ĐƯỢC

- alert_producer_bai3.py gửi 3 loại message: info, warning, critical
- warning_consumer_bai3.py chỉ nhận message có routing key warning
- critical_consumer_bai3.py chỉ nhận message có routing key critical
- Message info không được hai consumer trên nhận

Màn hình producer:
    Da gui [info]: He thong dang hoat dong binh thuong
    Da gui [warning]: Nhiet do phong may vuot nguong warning
    Da gui [critical]: Cam bien kho lanh mat ket noi critical

Màn hình warning consumer:
    [warning_queue] Da nhan: Nhiet do phong may vuot nguong warning

Màn hình critical consumer:
    [critical_queue] Da nhan: Cam bien kho lanh mat ket noi critical

6. GIẢI THÍCH

- Producer không gửi trực tiếp vào queue mà gửi vào exchange
- Direct exchange phân phối message dựa trên routing key
- warning_queue chỉ nhận routing key warning
- critical_queue chỉ nhận routing key critical
- info không có queue nào bind nên không được hai consumer trên nhận

7. LƯU Ý TƯƠNG THÍCH RABBITMQ 4.3.6

- Queue trong code sử dụng durable=True
- Exchange cũng được khai báo durable=True
- Giữ nguyên các khai báo này trong code