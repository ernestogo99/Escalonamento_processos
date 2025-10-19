from typing import List,Optional

from ..models import Process

def fcfs(ready:List[Process],time:int,prev_proc_id:Optional[str])->Optional[Process]:
    if not  ready:
        return None
    
    ready_sorted=sorted(ready,key=lambda p:p.arrival)
    return ready_sorted[0]
