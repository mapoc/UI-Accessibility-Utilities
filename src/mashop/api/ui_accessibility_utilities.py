def http_get(request, response, params):
    response.body = {"message": "hello world"}
