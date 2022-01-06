from quopri import decodestring

from .requests import PostRequests, GetRequests


class PageNotFound404:
    def __call__(self, request):
        return "404 WHAT", "404 PAGE Not Found"


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        # получаем параметры запроса
        path = environ["PATH_INFO"]
        method = environ["REQUEST_METHOD"]

        # добавление закрывающего слеша
        if not path.endswith("/"):
            path = f"{path}/"

        request = {
            "method": method,
            "url": path,
        }

        if method == "GET":
            data = GetRequests().get_request_params(environ)
            request["params"] = data
            if len(data) > 0:
                print(f"Пришёл get-запрос с параметрами: {data}")
        if method == "POST":
            data = PostRequests().get_request_params(environ)
            request["params"] = Framework.decode_value(data)
            print(f"Пришёл post-запрос с параметрами: {Framework.decode_value(data)}")

        # находим нужный контроллер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # этот словарь получат все контроллеры
        for front in self.fronts_lst:
            front(request)

        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace("%", "=").replace("+", " "), "UTF-8")
            val_decode_str = decodestring(val).decode("UTF-8")
            new_data[k] = val_decode_str
        return new_data
