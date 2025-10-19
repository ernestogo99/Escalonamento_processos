from ninja import Router
from .schemas import ProcessSchema,ResultSchema,SimulationInSchema
from .models import Process
from .services import run_simulation
from .algoritms.fcfs import fcfs

task_scheduling_router=Router(tags=['Escalonamento de tarefas'])



@task_scheduling_router.post('/',response={200:ProcessSchema})
def create_process(request,process:ProcessSchema):
    """Endpoint de demonstração do django ninja para os divos"""
    return process


@task_scheduling_router.get('/',response={200:dict})
def teste(request):
    """Teste"""
    dict={
        'id':1,
        'teste':'testando'
    }
    return dict


@task_scheduling_router.post('/schedule',response={200:ResultSchema,403:dict})
def schedule_task(request,data:SimulationInSchema):
    """
    Endpoint para executar o escalonamento de tarefas
    """
    processes=[Process(**p.dict()) for p in data.processes]

    if data.algorithm =='fcfs':
        return run_simulation(processes,fcfs)
    
    return {'error':'Algoritmo não encontrado'}
