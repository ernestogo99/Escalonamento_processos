
from typing import List, Optional
from ..models import Process



def round_robin(ready: List[Process], time: int, prev_proc_id: Optional[str], quantum: int) -> Optional[Process]: 
    if not ready:
        return None
    
    ready_sorted=sorted(ready,key=lambda p:p.arrival)
    current_process=ready_sorted[0]
    if current_process.remaining > quantum:
        current_process.remaining -=quantum
        ready_sorted.append(current_process)
    else:
        current_process.remaining=0
    
    return current_process



def round_robin_priority_aging(ready: List[Process], time: int, prev_proc_id: Optional[str], quantum: int,aging:int) -> Optional[Process]: 
   pass