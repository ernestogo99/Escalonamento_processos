from ninja import Router
from .schemas import ResultSchema,SimulationInSchema
from .models import Process
from .services import run_simulation
from .algoritms.fcfs import fcfs
from .algoritms.shortest_job_first import sjf
from .algoritms.shortest_remaining_time_first import srtf
from .algoritms.priority import priority_non_preemptive,priority_preemptive
from .algoritms.round_robin import round_robin,round_robin_priority_aging
from ninja.errors import HttpError

task_scheduling_router=Router(tags=['Escalonamento de tarefas'])

@task_scheduling_router.post('/schedule',response={200:ResultSchema,403:dict})
def schedule_task(request,data:SimulationInSchema):
    """
    Endpoint para executar o escalonamento de tarefas
    """
    
    ALGORITHMS = {
    'fcfs': fcfs,
    'sjf': sjf,
    'srtf': srtf,
    'pnp':priority_non_preemptive,
    'pp':priority_preemptive,
    'rr':round_robin,
    'rr_priority_aging':round_robin_priority_aging
    
}
    algorithm_func = ALGORITHMS.get(data.algorithm.lower())

    if not algorithm_func:
        raise HttpError(400, f"Algoritmo '{data.algorithm}' não é suportado.")

    try:
        processes = [Process(**p.dict()) for p in data.processes]
        if data.algorithm.lower() == 'rr':  
            quantum = data.quantum
            result = run_simulation(processes, algorithm_func, quantum,data.algorithm.lower()) 
        elif data.algorithm.lower() =='rr_priority_aging':
            quantum=data.quantum
            aging=data.aging
            result = run_simulation(processes, algorithm_func, quantum,data.algorithm.lower(),aging) 

        else:
            result = run_simulation(processes, algorithm_func,algoritm_name=data.algorithm.lower())  

        return result
    except Exception as e:
        raise HttpError(400, f"Erro ao executar simulação: {str(e)}")
