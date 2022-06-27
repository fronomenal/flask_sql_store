from werkzeug import Request, Response
from datetime import date, datetime

LOG_FILE = f"./logs/{date.today()}_cc.log"


class LogMiddleware:
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        resp = Response(start_response)
        self._process_request(req)
        self._process_response(resp)
        return self._app(environ, start_response)

    @staticmethod
    def _process_request(request):
        with open(LOG_FILE, 'a+', encoding='UTF-8') as f:
            cur_time = datetime.now().strftime("%H:%M:%S")
            f.write(f'{cur_time}  {request.path} request: {request.method}')

    @staticmethod
    def _process_response(response):
        with open(LOG_FILE, 'a+', encoding='UTF-8') as f:
            f.write(f' | response: {response.status_code}')
            f.writelines("\n")