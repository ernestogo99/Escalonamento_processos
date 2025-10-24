from ninja import Schema
from typing import List, Dict,Optional

class ProcessSchema(Schema):
    id:str
    arrival:int
    duration:int
    priority:int

  


class SimulationInSchema(Schema):
    algorithm:str
    processes:List[ProcessSchema]
    quantum:Optional[int] =None
    aging:Optional[int] = None

class TimelineEntrySchema(Schema):
    time:str
    state:Dict[str,str]

class ResultSchema(Schema):
    average_turnaround: float
    average_waiting: float
    context_switches: int
    timeline: List[TimelineEntrySchema]
