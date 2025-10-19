from typing import List,Optional
from ..models import Process

def sjf(ready:List[Process],time:int,prev_proc_id:Optional[str])-> Optional[Process]:
    if prev_proc_id:
        for p in ready:
            if p.id == prev_proc_id:
                return p
    if not ready:
        return None
    
    ready_process=min(ready,key=lambda p:p.remaining)
    return ready_process


