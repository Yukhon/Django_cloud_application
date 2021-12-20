from django.utils.deprecation import MiddlewareMixin


class MyMW(MiddlewareMixin):

    def process_request(self, request):
        print('Mymw process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Mymw process_views do ---')

    def process_response(self, request, response):
        print('MyMW process_response do ---')
        return response




class MyMW2(MiddlewareMixin):

    def process_request(self, request):
        print('Mymw2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Mymw2 process_views do ---')

    def process_response(self, request, response):
        print('MyMW2 process_response do ---')
        return response