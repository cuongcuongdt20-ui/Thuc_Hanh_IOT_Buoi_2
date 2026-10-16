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


__________BAI2_____________
Sinh viên: Nguyễn Doãn Hợp
MSV: B23DCCN350
BÀI 2: MÔ PHỎNG CẢM BIẾN IOT GỬI DỮ LIỆU MÔI TRƯỜNG

1. BROKER SỬ DỤNG

- RabbitMQ chạy trên máy cá nhân.
- Địa chỉ mặc định: localhost; cổng AMQP: 5672.
- Tài khoản mặc định: guest / guest; virtual host: /.
- Queue: sensor_data_queue, khai báo durable=True ở cả hai chương trình.
- Thư viện Python: pika.
- Nếu dùng broker của lớp, sửa BROKER, PORT, USERNAME, PASSWORD, VHOST
  ở đầu CẢ HAI file Python thành cùng cấu hình. Tài khoản guest mặc định
  chỉ dùng để kết nối cục bộ; broker từ xa cần tài khoản được cấp.

2. CÁC FILE VÀ CHỨC NĂNG

- sensor_producer_bai2.py:
  + Mô phỏng thiết bị sensor01.
  + Sinh ngẫu nhiên nhiệt độ từ 20 đến 40 độ C, độ ẩm từ 30 đến 80%.
  + Làm tròn đến một chữ số thập phân.
  + Gửi JSON vào sensor_data_queue mỗi 3 giây qua default exchange.
  + Payload gồm device_id, temperature, humidity. Ví dụ:
    {"device_id": "sensor01", "temperature": 36.4, "humidity": 38.9}

- monitor_consumer_bai2.py:
  + Lắng nghe sensor_data_queue liên tục.
  + Phân tích JSON và in mã thiết bị, nhiệt độ, độ ẩm.
  + Nhiệt độ > 35: in "CANH BAO: Nhiet do cao".
  + Độ ẩm < 40: in "CANH BAO: Do am thap".
  + Hai điều kiện được kiểm tra độc lập, có thể xuất hiện cả hai cảnh báo.
  + Nhiệt độ bằng 35 và độ ẩm bằng 40 không kích hoạt cảnh báo tương ứng.
  + Xác nhận message sau khi xử lý; message sai định dạng bị loại bỏ và
    thông báo lỗi, consumer tiếp tục chờ message tiếp theo.

3. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH

Chuẩn bị:
- Cài Python 3 và khởi động RabbitMQ trước khi chạy.
- Cài thư viện bằng lệnh:
    python -m pip install pika
- Trên Windows, nếu không gọi được python, thay python bằng py.

Mở hai terminal, mỗi terminal bắt đầu ở thư mục gốc dự án.

Terminal 1 - chạy monitoring consumer:
    cd Bai_2
    python monitor_consumer_bai2.py

Terminal 2 - chạy sensor producer:
    cd Bai_2
    python sensor_producer_bai2.py

Nhấn Ctrl+C ở từng terminal để dừng chương trình và đóng kết nối.
Có thể chạy producer trước: queue lưu message chờ consumer nhận.
Nếu không kết nối được, kiểm tra RabbitMQ đã chạy, cổng 5672 và thông tin
đăng nhập trong cả hai file. Nếu báo thiếu pika, chạy lại lệnh cài ở trên.
Nếu queue đã tồn tại với durable=False, cần dùng queue có cấu hình thống
nhất; chỉ xóa và tạo lại queue cũ khi không cần giữ các message trong đó.

4. KẾT QUẢ VÀ ĐẦU RA MINH HỌA

Khi chạy với RabbitMQ, chương trình thực hiện các yêu cầu:
- Producer gửi dữ liệu JSON ngẫu nhiên định kỳ mỗi 3 giây.
- Consumer nhận và hiển thị đủ ba trường dữ liệu.
- Consumer phát hiện nhiệt độ cao và độ ẩm thấp theo đúng ngưỡng đề bài.

Ví dụ màn hình producer:
    Dang gui du lieu moi 3 giay - nhan Ctrl+C de dung
    Da gui: {"device_id": "sensor01", "temperature": 36.4, "humidity": 38.9}

Ví dụ màn hình consumer:
    Dang cho du lieu tu sensor_data_queue - nhan Ctrl+C de dung
    Device: sensor01
    Temperature: 36.4
    Humidity: 38.9
    CANH BAO: Nhiet do cao
    CANH BAO: Do am thap
    ----------------------------------------

Đây là đầu ra minh họa; số đo thực tế thay đổi do sinh ngẫu nhiên.
Để kiểm tra truyền nhận thực tế, chạy cả hai chương trình theo mục 3,
đối chiếu số đo producer gửi với số đo consumer nhận trong từng message.


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