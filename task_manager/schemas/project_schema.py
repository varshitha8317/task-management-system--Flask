from marshmallow import Schema,fields
class ProjectSchema(Schema):
    name=fields.Str(required=True)