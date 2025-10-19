from ninja import Schema


class ProcessSchema(Schema):
    id:str
    arrival:int
    duration:int
    priority:int



