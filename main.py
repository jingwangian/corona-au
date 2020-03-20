from app import app
from app.components.main_page import get_main_page

if __name__ == '__main__':
    app.layout = get_main_page()

    app.run_server(host='0.0.0.0', debug=True)
