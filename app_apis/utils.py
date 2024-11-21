import jwt
from django.conf  import settings
def generate_token(user_id, phone):
    payload = {
        'user_id': user_id,
        'phone': phone,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token