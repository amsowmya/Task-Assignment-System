from Service.task_service import Task_Service
from Service.user_service import User_Service


def main():
    task_service = Task_Service()
    user_service = User_Service()
    
    user_service.add_user(123, 'Sam', 'sam@awesome.com')
    task_service.create_task(1, "Teach Data Strcture basic", "Teach from Scratch")
    task_service.create_task(2, "Teach Advance Data Strcture basic", "Teach from Scratch")
    task_service.create_task(3, "Do a project", "Teach from Scratch")
    
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    
    history = task_service.get_task_history()
    
    print("History")
    print(history.pop().title)
    print(history.pop().title)
    print(history.pop().title)
        

if __name__ == "__main__":
    main()