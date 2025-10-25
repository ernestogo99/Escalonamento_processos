
from typing import List, Optional
from ..models import Process
from collections import deque





rr_queue = deque()



def round_robin(ready: List[Process], time: int, prev_proc_id: Optional[str], quantum: int) -> Optional[Process]:
    """
    Seleciona o próximo processo a ser executado usando o algoritmo Round Robin (RR).

    Este algoritmo mantém uma fila circular (deque) de processos prontos. Cada processo 
    executa por no máximo `quantum` unidades de tempo antes de ser movido para o final 
    da fila, permitindo que outros processos sejam executados de forma justa.

    O contador interno `_slice` em cada processo serve controlar quantos ticks do quantum já foram 
    consumidos. Se o processo terminar, ele  é removido da fila. 
    Novos processos que chegam no tempo atual são adicionados à fila.

    :param ready: Lista de processos prontos (objetos Process) que chegaram até o tempo atual.
    :param time: Tempo atual da simulação.
    :param prev_proc_id: ID do processo que estava rodando no tick anterior (pode ser None).
    :param quantum: Número máximo de ticks que um processo pode executar antes de ser rotacionado.
    :return: O processo que deve executar neste tick, ou None se nenhum processo estiver pronto.
    """

    global rr_queue

  
    for p in ready:
        if p not in rr_queue and p.remaining > 0:
            rr_queue.append(p)

    if not rr_queue:
        return None

    current = rr_queue[0]

    if not hasattr(current, "_slice"):
        current._slice = 0


    if current.remaining == 0:
        rr_queue.popleft()
        if rr_queue:
            current = rr_queue[0]
            if not hasattr(current, "_slice"):
                current._slice = 0
        else:
            return None

    return current



def round_robin_priority_aging(ready: List[Process]                               
, time: int
, prev_proc_id: Optional[str]
,quantum: int
, aging: int) -> Optional[Process]:
    """
    Round-Robin com prioridade e envelhecimento (aging)

   
   
    :param ready: Lista de processos prontos que chegaram até o tempo atual.
    :param time: Tempo atual da simulação.
    :param prev_proc_id: ID do processo que estava rodando no tick anterior (pode ser None).
    :param quantum: Quantum usado no RR.
    :param aging: Valor a ser adicionado à prioridade dos processos inativos.
    :return: O próximo processo a executar ou None se nenhum processo estiver pronto.
    """
    global rr_queue
  
    for p in ready:
        if p not in rr_queue and p.remaining > 0:
            rr_queue.append(p)

    while rr_queue and rr_queue[0].remaining <= 0:
        rr_queue.popleft()
    if not rr_queue:
        return None

    rr_queue = deque(sorted(rr_queue, key=lambda x: (x.priority, x.arrival)))
    return rr_queue[0]
