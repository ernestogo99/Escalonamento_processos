from typing import List,Optional
from ..models import Process 

def priority_non_preemptive(ready: List[Process], time: int, prev_proc_id: Optional[str]) -> Optional[Process]:
    """
    Algoritmo de Prioridade Não-Preemptivo.

    O processo com maior prioridade (menor valor numérico) é escolhido para execução,
    mas uma vez que começa a rodar, ele continua até terminar — não é interrompido 
    mesmo que um processo com prioridade maior chegue depois.

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

   
    selected = sorted(ready, key=lambda p: (p.priority, p.arrival))
    return selected[0]


def priority_preemptive(ready: List[Process], time: int, prev_proc_id: Optional[str]) -> Optional[Process]:
    """
    Algoritmo de Prioridade Preemptivo.

    O processo com maior prioridade (menor valor numérico) é sempre escolhido.
    Se um novo processo com prioridade mais alta chega, ele interrompe (preempção)
    o processo atualmente em execução.

    :param ready: Lista de processos prontos (objetos da classe Process)
    :param time: Tempo atual da simulação (não utilizado diretamente)
    :param prev_proc_id: ID do processo que estava executando anteriormente (pode mudar a cada instante)
    :return: O processo que deve ser executado no instante atual
    """
 
    if not ready:
        return None
    
    selected = sorted(ready, key=lambda p: (p.priority, p.arrival))
    return selected[0]
