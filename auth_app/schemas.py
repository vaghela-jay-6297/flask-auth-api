# User_app/schemas.py
from marshmallow import Schema, fields, validate, validates, ValidationError
from .models import User

class UserSerializer(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1), error_messages={"required": "Name is required!"})
    email = fields.Email(required=True, error_messages={"required": "Email is required!"})
    gender = fields.Str(required=True, validate=validate.OneOf(["M", "F"]), error_messages={"required": "Gender is required!"})
    phone_number = fields.Str(required=True, validate=validate.Length(min=10, max=15), error_messages={"required": "Phone number is required!"})
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6), error_messages={"required": "Password is required!"})
    created_on = fields.DateTime(dump_only=True)
    updated_on = fields.DateTime(dump_only=True)
    is_delete = fields.Bool(dump_only=True)
    is_active = fields.Bool(dump_only=True)

    @validates('email')
    def validate_email(self, value):
        existing_user = User.query.filter_by(email=value).first()
        if existing_user:
            raise ValidationError('Email address already exists!')

    @validates('phone_number')
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise ValidationError('Phone number must contain only digits!')
        if not value.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            raise ValidationError('Phone number must start with a valid digit!')
