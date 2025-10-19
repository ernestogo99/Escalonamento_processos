from typing import List,Optional
from ..models import Process


def srtf(ready:List[Process],time:int,prev_proc_id:Optional[str])->Optional[str]:
    if not ready:
        return None
    ready_process=min(ready,key=lambda p:p.remaining)
    return ready_process
