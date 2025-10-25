## Escalonamento de Processos

O objetivo deste projeto é escrever um programa para simular o escalonamento de um conjunto
de tarefas usando os algoritmos de escalonamento de processador mais conhecidos

## Equipe

- Ernesto Dalva
- Ramon Nicolas
- Diogo Santiago
- July Santiago
- Diego Rabelo

## Tecnologias utilizadas

- Python: Linguagem de programação para o back-end
- DJango Ninja: Framework utilizado para o desenvolvimento de apis
- Typescript: Linguagem escolhida para o front-end
- React: Biblioteca de componentes utilizada para o front-end

## Relatório

Escolhemos a seguinte classe para representar o processo:

```python
class Process:
    def __init__(self, id, arrival, duration, priority):
        self.id = id
        self.arrival = arrival
        self.duration = duration
        self.priority = priority

        self.remaining = duration
        self.start = None
        self.finish = None

    def __str__(self):
        return self.id
```

Essa classe foi escolhida com o objetivo de representar um processo
e poder manipulá-lo da melhor forma ao simular um escalonamento de processos

Schemas:
Utilizados para tipar no python

```python

class ProcessSchema(Schema):
    id:str
    arrival:int
    duration:int
    priority:int

class SimulationInSchema(Schema):
    algorithm:str
    processes:List[ProcessSchema]
    quantum:Optional[int] =None
    aging:Optional[int] = None

class TimelineEntrySchema(Schema):
    time:str
    state:Dict[str,str]

class ResultSchema(Schema):
    average_turnaround: float
    average_waiting: float
    context_switches: int
    timeline: List[TimelineEntrySchema]
```

O ProcessSchema representa o processo.
O SimulationInSchema representa a entrada que será passada ao front-end
O TimelineEntrySchema representa a timeline
O ResultSchema representa o resultado da simulação do escalonamento de processos

Observação: Nas pastas de back-end e de front-end se encontram um readme com a estrutura de pastas
e como rodar o projeto.
