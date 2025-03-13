import sys

sys.path.append("./")
from release_scheduler.scheduler import Scheduler
from gitlabjob_generator.generator import Generator

if __name__ == "__main__":
    choice=input("1: Generate a GitLabJob\n2: Debug a GitLabJob\n3: Get product release suggestions ")
    if choice == "1":
        generator_instance = Generator()
        generator_instance.GenerateJob()
    elif choice == "3":
        scheduler_instance = Scheduler()
        scheduler_instance.GetSchedule()
