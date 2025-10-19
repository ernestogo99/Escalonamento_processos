from ninja import Router
from .schemas import ProcessSchema,ResultSchema,SimulationInSchema
from .models import Process
from .services import run_simulation
from .algoritms.fcfs import fcfs
from .algoritms.shortest_job_first import sjf
from .algoritms.shortest_remaining_time_first import srtf
from ninja.errors import HttpError

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
    ALGORITHMS = {
    'fcfs': fcfs,
    'sjf': sjf,
    'srtf': srtf
}
    algorithm_func = ALGORITHMS.get(data.algorithm.lower())

    if not algorithm_func:
        raise HttpError(400, f"Algoritmo '{data.algorithm}' não é suportado.")

    try:
        processes = [Process(**p.dict()) for p in data.processes]
        result = run_simulation(processes, algorithm_func)
        return result
    except Exception as e:
        raise HttpError(400, f"Erro ao executar simulação: {str(e)}")
