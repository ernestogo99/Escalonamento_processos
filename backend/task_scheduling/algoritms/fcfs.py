from typing import List

from ..models import Process

def fcfs(ready: List[Process],*_args) -> Process:
    if not  ready:
        return None
    
    ready_sorted=sorted(ready,key=lambda p:p.arrival)
    return ready_sorted[0]
