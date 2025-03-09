import sys

sys.path.append("./")
from auth import authenticator
import datetime
import release_scheduler.scheduler
from release_scheduler.scheduler import Scheduler

if __name__ == "__main__":
    choice=input("1: Generate a ProwJob\n2: Debug a ProwJob\n3: Get product release suggestions ")
    if choice == "1":
        scheduler_instance = Scheduler()
        scheduler_instance.GetSchedule()
