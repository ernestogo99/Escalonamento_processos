from typing import List,Optional

from ..models import Process

def fcfs(ready: List[Process], time: int, prev_proc_id: Optional[str]) -> Optional[Process]:
    """
    Algoritmo First Come, First Served (FCFS).

    Seleciona o processo que chegou primeiro na fila de prontos, 
    sem preempção (não interrompe o processo em execução).

    :param ready: Lista de processos prontos (objetos da classe Process)
    :param time: Tempo atual da simulação (não utilizado neste algoritmo)
    :param prev_proc_id: ID do processo que estava executando anteriormente (não utilizado no FCFS)
    :return: O processo que deve ser executado (primeiro a chegar)
    """
    if not ready:
        return None

    ready_sorted = sorted(ready, key=lambda p: p.arrival)
    return ready_sorted[0]

