from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Kết quả thực hành PaaS trên Render thành công!</h1><p>Ứng dụng Python Flask đang chạy trên môi trường đám mây.</p>"

if __name__ == '__main__':
    app.run(debug=True)
