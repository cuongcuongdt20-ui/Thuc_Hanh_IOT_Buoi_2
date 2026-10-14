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
