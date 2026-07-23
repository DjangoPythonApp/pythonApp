import uuid

# Global Middleware
class RequestReferenceMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.reference_id = ("REQ-" +str(uuid.uuid4())[:6].upper())
        response = self.get_response(request)
        return response
    

# Specific url middleware with url: ['/', '/success/']
# class RequestReferenceMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path in ['/', '/success/']:
#             request.reference_id = ("REQ-" +str(uuid.uuid4())[:6].upper())
        
#         response = self.get_response(request)
#         return response