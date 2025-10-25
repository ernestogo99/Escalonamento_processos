from typing import List,Optional
from ..models import Process


def srtf(ready: List[Process], time: int, prev_proc_id: Optional[str]) -> Optional[Process]:
    """
    Algoritmo Shortest Remaining Time First (SRTF) — Preemptivo.

    Variante preemptiva do SJF. Escolhe sempre o processo com o menor tempo restante de execução.
    Caso um novo processo chegue com tempo menor que o do processo atual, ocorre preempção
    (interrupção do processo em execução).

    :param ready: Lista de processos prontos (objetos da classe Process)
    :param time: Tempo atual da simulação
    :param prev_proc_id: ID do processo que estava executando anteriormente (não usado aqui)
    :return: O processo com o menor tempo restante (aquele que deve executar no instante atual)
    """

    if not ready:
        return None


    ready_process = min(ready, key=lambda p: p.remaining)

    return ready_process

