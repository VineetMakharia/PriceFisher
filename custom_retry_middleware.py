from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
# from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware


class CustomRetryMiddleware(RetryMiddleware):

    def __init__(self, settings):
        RetryMiddleware.__init__(self, settings)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response

        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider)

        # this is your check
        if response.status == 200 and response.xpath(spider.retry_xpath).extract() == []:
            # return response.xpath(spider.retry_xpath)
            # return "pleasestartworking"
            return self._retry(request, 'product name and price response is empty', spider)
        return response