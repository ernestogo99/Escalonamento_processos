from typing import List,Optional
from ..models import Process 

def priority_non_preemptive(ready:List[Process],time:int,prev_proc_id:Optional[str])->Optional[Process]:
    if prev_proc_id:
        for p in ready:
            if p.id == prev_proc_id:
                return p
    if not ready:
        return None
    
    selected=sorted(ready,key=lambda p:(p.priority,p.arrival))
    return selected[0]


def priority_preemptive(ready:List[Process],time:int,prev_proc_id:Optional[str])->Optional[Process]:
    if not ready:
        return None
    
    selected=sorted(ready,key=lambda p:(p.priority,p.arrival))
    return selected[0]