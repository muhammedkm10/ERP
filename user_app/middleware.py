from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import jwt
from django.conf  import settings
from jwt.exceptions import InvalidTokenError
from .models import ShopOwners

class TokenAuthMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # Initialize any other state if needed, like logging or other configurations

    def __call__(self, request):
        # Middleware logic goes here, this is called before the request reaches the view
        excluded_urls = ['/api/user_login',]
        
        if request.path.startswith("/admin/") or request.path.startswith("/client") or request.path == "/":
            response = self.get_response(request)
            return response
        if request.method == "POST" and request.path in excluded_urls:
            response = self.get_response(request)
            return response
        
        
        
        # Get the token from the Authorization header (Bearer token)
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({"error": "Token is missing"}, status=401)
       
        
        token = auth_header.split(' ')[1]
        is_valid = self.validate_token(token)
        if not is_valid:
            return JsonResponse({"error": "Invalid token"}, status=401)
        # Once validated, call the next middleware or view
        request.user_id = is_valid["user_id"]
        user = ShopOwners.objects.get(id = is_valid["user_id"])
        if user.block:
            return JsonResponse({"error": "you are blocked"}, status=401)
        request.phone = is_valid["phone"]
        response = self.get_response(request)
        return response
    
    def validate_token(self,token):
        try:
            # Decode the token using the SECRET_KEY and HS256 algorithm
            decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # If decoding is successful, the token is valid
            return decoded_payload  # Return the decoded payload (user info)
        
        
        except InvalidTokenError:
            # Handle invalid token case (e.g., wrong signature or tampered token)
            return False
        
        except Exception as e:
            # Handle any other exceptions (general error logging)
            return False