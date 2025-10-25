from typing import List,Optional
from ..models import Process

def sjf(ready: List[Process], time: int, prev_proc_id: Optional[str]) -> Optional[Process]:
    """
    Algoritmo Shortest Job First (SJF) — Não-Preemptivo.

    Escolhe para execução o processo com o menor tempo restante de CPU (menor duração total).
    Uma vez iniciado, o processo continua até terminar, mesmo que outro mais curto chegue depois.

    :param ready: Lista de processos prontos (objetos da classe Process)
    :param time: Tempo atual da simulação (não utilizado diretamente)
    :param prev_proc_id: ID do processo que estava executando anteriormente
    :return: O processo que deve ser executado no instante atual
    """
 
    if prev_proc_id:
        for p in ready:
            if p.id == prev_proc_id:
                return p

    if not ready:
        return None


    ready_process = min(ready, key=lambda p: p.remaining)
    return ready_process



