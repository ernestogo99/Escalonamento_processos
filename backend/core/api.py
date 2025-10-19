from ninja import NinjaAPI
from task_scheduling.api import task_scheduling_router

api=NinjaAPI(title="Scheduler task API")


api.add_router('scheduling/',task_scheduling_router)