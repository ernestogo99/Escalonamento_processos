from typing import List, Dict
from ..schemas import ProcessSchema

def fcfs(ready: List[ProcessSchema],*_args) -> Dict:
    if not  ready:
        return None
    
    ready_sorted=sorted(ready,key=lambda p:p.arrival)
    return ready_sorted[0]
