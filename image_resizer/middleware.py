import logging


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("middleware")

    def __call__(self, request):
        self.logger.info(f"Request: {request.method} {request.path} {request.POST.dict()}")

        response = self.get_response(request)

        content = response.content.decode("utf-8")
        self.logger.info(f"Response: {response.status_code} {response.reason_phrase} {content}")

        return response
