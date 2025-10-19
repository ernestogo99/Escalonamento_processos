from ninja import Router
from .schemas import ProcessSchema

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