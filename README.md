# Tính năng
- Mặc định in ra toàn bộ thông tin headers và payload của request và response.
- Có thể tùy chọn lấy ra 1 trong số các field của Request header và Response Payload (nếu Response Payload ở dạng json)
- Có thể tùy chọn log các thông tin ra file


# Hướng dẫn sử dụng

- Tạo môi trường ảo: python3 -m venv venv
- Truy cập môi trường ảo: source venv/bin/activate
- Cài đặt thư viện Flask: pip install flask
- Cài đặt middleware: pip install git+https://github.com/ngocvinhvu/logging_middleware.git#egg=LoggingMiddleware
- Thêm vào file app.py của bạn:

from LoggingMiddleware import loggingrequest, loggingresponse

app = Flask(__name__)

app.before_request(loggingrequest)
app.after_request(loggingresponse)
'''
config
'''
@app.route(/)...

# Cách Config:
- Config field Request header:

Nếu bạn muốn bất cứ field nào trong header của mình không hiển thị:
Thêm "app.config['tên field'] = False" vào phần (config)
Ví dụ: app.config['Cookie'] = False trường Cookie sẽ không hiển thị.

- Config log vào file:

Nếu bạn muốn log thông tin của Request vào file: 
Thêm "app.config['LOG_REQUEST'] = True" vào (config)
Tương tự nếu muốn log thông tin của Response vào file:
Thêm app.config['LOG_RESPONSE'] = True vào (config)
Thông tin sẽ được lưu vào file logging.log
