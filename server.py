from waitress import serve
from suppliers.wsgi import application

if __name__ == '__main__':
    print("Open browser in http://localhost:8080")
    print("Shut down server with 'control + c'")
    serve(application, host='127.0.0.1', port=8080)
