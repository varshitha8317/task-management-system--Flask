from marshmallow import Schema,fields,validate

class TaskCreateSchema(Schema):
    title=fields.Str(required=True)
    description=fields.Str()
    priority=fields.Str(validate=validate.OneOf(["low","medium","high"]))
    due_date=fields.Date()
    project_id=fields.Int()
    assigned_user_ids=fields.List(fields.Int())

class TaskUpdateSchema(Schema):
    title=fields.Str()
    description=fields.Str()
    priority=fields.Str(validate=validate.OneOf(["low","medium","high"]))
    status=fields.Str(validate=validate.OneOf(["pending","In-progress","Completed"]))