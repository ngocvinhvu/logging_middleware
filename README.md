# Tính năng

- Mặc định hiển thị info header, payload của request và response
- Tùy chọn tắt hiển thị một hay nhiều field trong request header
- Tùy chọn tắt hiển thị một hay nhiều field trong response payload nếu payload ở định dạng json
- Tùy chọn log các thông tin vào file

# Hướng dẫn sử dụng

- Tạo môi trường ảo: python3 -m venv venv
- Truy cập môi trường ảo: source venv/bin/activate
- Cài đặt thư viện Flask: pip install flask
- Cài đặt middleware: pip install git+https://github.com/ngocvinhvu/logging_middleware.git#egg=LoggingMiddleware
- Thêm vào file app.py của bạn:

- from LoggingMiddleware import loggingrequest, loggingresponse
- app = Flask(...)
- app.before_request(loggingrequest)
- app.after_request(loggingresponse)
- <phần config>
- @app.route('/')...

# Cách Config:
- Config mặc định là hiển thị toàn bộ các trường và không lưu vào file 
- Config field Request header:

Thêm "app.config['tên field'] = False" vào phần config để không hiển thị field đó
Ví dụ: app.config['Cookie'] = False trường Cookie sẽ không hiển thị.

- Config field Response payload:

Thêm "app.config['tên field'] = False" vào phần config để không hiển thị field đó
Ví dụ: app.config['id'] = False trường id sẽ không hiển thị.

- Config log vào file:

Thêm "app.config['LOG_REQUEST'] = True" vào phần config để add info của Request

Thêm "app.config['LOG_RESPONSE'] = True" vào phần config để add info của R

Thông tin sẽ được lưu vào file logging.log
