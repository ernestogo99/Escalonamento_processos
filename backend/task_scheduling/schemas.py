from ninja import Schema
from typing import List, Dict

class ProcessSchema(Schema):
    id:str
    arrival:int
    duration:int
    priority:int
  


class SimulationInSchema(Schema):
    algorithm:str
    processes:List[ProcessSchema]

class TimelineEntrySchema(Schema):
    time:str
    state:Dict[str,str]

class ResultSchema(Schema):
    average_turnaround: float
    average_waiting: float
    context_switches: int
    timeline: List[TimelineEntrySchema]
