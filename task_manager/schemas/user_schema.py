from marshmallow import Schema,fields,validate
class UserRegisterSchema(Schema):
    name=fields.Str(required=True)
    email=fields.Email(required=True)
    password=fields.Str(required=True,validate=validate.Length(min=6))
    role=fields.Str(required=True,validate=validate.OneOf(["admin","manager","employee"]))

    department_id=fields.Int(required=False)

class UserLoginSchema(Schema):
    email=fields.Email(required=True)
    password=fields.Str(required=True)
    
