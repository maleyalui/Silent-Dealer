from flask import Blueprint, jsonify

student_bp = Blueprint('student', __name__)

@student_bp.route("/", methods=["GET"])
async def list_students():
    return jsonify({"message": "List of students"}), 200
    # prisma = Prisma()
    # await prisma.connect()
    
    # student = await prisma.student.find_first()
    
    # student_dict = student.model_dump()
         
    # return jsonify(student_dict), 200

@student_bp.route("/<int:student_id>", methods=["GET"])
async def get_student(student_id):
    return jsonify({"message": f"Get student with ID {student_id}"}), 200

@student_bp.route("/", methods=["POST"])
async def create_student():
    return jsonify({"message": "Create a new student"}), 201

@student_bp.route("/<int:student_id>", methods=["PUT"])
async def update_student(student_id):
    return jsonify({"message": f"Update student with ID {student_id}"}), 200