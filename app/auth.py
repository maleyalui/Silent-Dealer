import re # for regex validation
from flask import Blueprint, request, jsonify
from prisma import Prisma
from app.bcrypt import bcrypt
from app.jwt import generate_token, require_auth
from app.prisma import with_prisma

auth_bp = Blueprint("auth_bp",__name__)

@auth_bp.route("/login", methods=["POST"])
@with_prisma
async def login(prisma):
    
    data = request.get_json()
    
    if not data:
        return "Invalid request data", 400
    
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return "Please provide email and password", 400
    
    player = await prisma.player.find_unique(
        where={
            "email": email
        },
        include={
            "player_password": True
        }
    )
    if not player:
        return "Player with {email} does not exist", 401
    
    player_password = player.player_password
    
    if not player_password:
        return "Password not set", 500
    
    is_valid = bcrypt.check_password_hash(player_password.password,password)
    
    if not is_valid:
        return "Invalid email or password", 401
    
    token = generate_token(player.id)
    
    return jsonify({"player": player.model_dump(), "token": token})

@auth_bp.route("/test",methods=["GET"])
@with_prisma
@require_auth
async def test_jwt(_jwt,prisma):
    print("USER DATA IS",_jwt)
    return "testing jwt"


@auth_bp.route("/signup", methods=["POST"])
@with_prisma
async def signup(prisma):
    
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if not name or not email or not password:
        return "Please provide name, email and password", 400
    
    if len(password) < 3:
        return "Password must be at least 3 characters long", 400
    
    # using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format", 400
    
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    
    #if email exists
    player_exist = await prisma.player.find_unique(
        where={
            "email": email
        }
    )
    if player_exist:
        return "Email already exists", 400
    
    transaction = None
    
    async with prisma.tx() as tx:
        new_player = await tx.player.create(
            data={
                "name": name,
                "email": email,
            }
        )
        
        new_player_pass = await tx.player_password.create(
            data={
                "password": hashed_password,
                "player_id": new_player.id
            }
        )
        
        transaction = new_player, new_player_pass
    
    return jsonify(transaction.model_dump())