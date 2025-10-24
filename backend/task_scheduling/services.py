
from typing import List, Callable, Optional
from .models import Process
from .schemas import ResultSchema, TimelineEntrySchema




def run_simulation(
    processes: List[Process],
    algorithm: Callable[[List[Process], int, Optional[str]], Optional[Process]],
    quantum:Optional[int]=None,
    algoritm_name: Optional[str] = None,
    aging:Optional[int]=None
) -> ResultSchema:
    """
    Simula o escalonamento de processos com base no algoritmo fornecido.

    :param processes: Lista de processos (classe interna Process)
    :param algorithm: Função que escolhe o próximo processo a executar
    :param quantum: Quantum usado em RR (opcional)
    :param algoritm_name: Nome do algoritmo, ex: 'fcfs', 'rr', 'rr_priority_aging'
    :param aging: Parâmetro de envelhecimento (opcional)
    :return: ResultSchema com estatísticas e timeline
    """
  
    time = 0
    finished = []
    context_switches = 0
    prev_proc_id = None
    timeline = []


    for p in processes:
        p.remaining = p.duration

    while len(finished) < len(processes):
      
        ready = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if algoritm_name == 'rr':
            current=algorithm(ready,time,prev_proc_id,quantum)
        
        elif algoritm_name =='rr_priority_aging':
            current=algorithm(ready,time,prev_proc_id,quantum,aging)
        else:
            current = algorithm(ready, time, prev_proc_id)
        

      
        state = {p.id: "--" for p in processes}

        if current:
            state[current.id] = "##"
            current.remaining -= 1

      
            if current.start is None:
                current.start = time

       
            if current.remaining == 0:
                current.finish = time + 1
                finished.append(current)

       
            if prev_proc_id and prev_proc_id != current.id:
                context_switches += 1

            prev_proc_id = current.id
        else:
          
            prev_proc_id = None

      
        timeline.append(
            TimelineEntrySchema(
                time=f"{time}-{time+1}",
                state=state
            )
        )

        time += 1


    n = len(processes)
    total_turnaround = sum(p.finish - p.arrival for p in processes)
    total_waiting = sum((p.finish - p.arrival - p.duration) for p in processes)

    avg_turnaround = round(total_turnaround / n, 2)
    avg_waiting = round(total_waiting / n, 2)

    return ResultSchema(
        average_turnaround=avg_turnaround,
        average_waiting=avg_waiting,
        context_switches=context_switches,
        timeline=timeline
    )
