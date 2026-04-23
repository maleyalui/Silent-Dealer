import token
import jwt
import os
from datetime import datetime,timedelta
from functools import wraps
from flask import request, jsonify

SECRECT_KEY = os.getenv("JWT_SECRET")
ALGORITHIM = "HS256"

def generate_token(id):
    now = datetime.utcnow()
    payload = {
        "id": id,
        "exp": now + timedelta(hours=3),
        "iat": now
    }
    token = jwt.encode(payload, SECRECT_KEY, algorithm=ALGORITHIM)
    return token

def verify_token():
    try:
        decoded = jwt.encode(token, SECRECT_KEY, algorithms=[ALGORITHIM])
        return decoded
    except:
        return None
    
def require_auth(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return "Authorization header is missing", 401   
        
        print("Auth header is",auth_header)
        
        try:
            split_token = auth_header.split(" ")
            print("Split token is",split_token)
            token_type = split_token[0]
            token_value = split_token[1]
            
            if token_type != "Bearer":
                return "Invalid token type", 401
            
            decoded= verify_token(token_value)
            
            if not decoded:
                return "Invalid or expired token", 401
            
            prisma = kwargs.get("prisma")
            _decoded_user = decoded
            
            if prisma:
                _decoded_user = await prisma.player.find_unique(
                    where={
                        "id": decoded["id"]
                    }
                )
                
            return await func(*args, jwt = _decoded_user, **kwargs)
        
        except Exception as e:
            print("Error in require_auth:", e)
            return "Invalid token format", 401
        
    return wrapper