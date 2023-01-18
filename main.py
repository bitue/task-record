import uuid 
from datetime import datetime


class Task :
    def __init__(self, task ) -> None:
        self.task = task
        self.created_at = datetime.now()
        self.updated_at = 'N\A'
        self.completed_at = 'N\A'
        self.task_done = False
        self.id = uuid.uuid1()

    def __repr__(self) -> str:
        return f'ID-{self.id} \nTask - {self.task} \nCreated time - {self.created_at} \nUpdated time : {self.updated_at} \nCompleted : {self.task_done} \nCompleted time - {self.completed_at}\n'
    

    def update_task(self, task_name):
        self.task = task_name
        self.updated_at = datetime.now()
        print('Update task successful')

    def complete_task(self):
        self.task_done = True 
        self.completed_at = datetime.now()
        print('Completed task successful')



class Task_list :
    tasks =[] 
    

    def __init__(self) -> None:
        pass

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print('Task added successful')
    
    def show_all_tasks (self):
        for i in self.tasks :
            print(i)
            print('\n')
    
    def show_all_tasks_before (self):
       
        
        for i in range(0, len(self.tasks)) :
            print(f'task no : {i+1}')
            print(self.tasks[i])
    
    def make_update_task(self):

        incomplete_tasks =  self.get_incomplete_task()
        if(len(incomplete_tasks) ==0):
            print("No Task to update ")
        
        else :
            for i in range(0, len(incomplete_tasks)):
                print(f"Task no {i+1}")
                print(incomplete_tasks[i])
            print("Enter the task Number : ")
            idx = int(input())

            print("Enter the task : ")
            name = input()
            get_task = incomplete_tasks[idx-1]
            getID = get_task.id 
            for t in self.tasks :
                if t.id == getID :
                    t.update_task(name)
           
       
    
    def make_complete_task(self):
        incomplete_tasks =  self.get_incomplete_task()
        if(len(incomplete_tasks) ==0):
            print("No Task to complete ")
        
        for i in range(0, len(incomplete_tasks)):
                print(f"Task no {i+1}")
                print(incomplete_tasks[i])



       
        print("Enter the task Number : ")
        idx = int(input())

       
        get_task = self.tasks[idx-1]
        getID = get_task.id 
        for t in self.tasks:
            if t.id == getID:
                t.complete_task()
       

        # self.completed_tasks.append(get_task)
    

    def show_completed_task(self):

        taskCm =[]

        for task in self.tasks:
            if task.task_done == True :
                taskCm.append(task)
        
        if len(taskCm)==0 :
            print('No task completed yet !')
        else :
            for t in taskCm :
                print(t)
            

        

    def get_incomplete_task(self):
        taskIn =[]

        for task in self.tasks :
            if task.task_done == False :
                taskIn.append(task)
        
        return taskIn
    
    def show_incomplete_task(self):
        incomplete_tasks = self.get_incomplete_task()
        if len(incomplete_tasks) ==0 :
            print("No Incomplete task ")
        else :
            for task in incomplete_tasks :
                print(task)

    
   
        
        

def display_always():
    return (f'1. Add New Task \n2. Show All tasks\n3. Show Incomplete tasks\n4. Show Completed Tasks \n5. Update Task\n6. Mark A Task Completed\n')


run = Task_list() 

while True :
    print(display_always())
    print("Enter the Option : ")
    opt = int(input())
    if(opt == 1):
        print('Enter the task name')
        name = input()
        run.add_task(name)
    elif(opt ==2):
        run.show_all_tasks()
    elif(opt == 3):
        run.show_incomplete_task()
    elif opt ==4 :
        run.show_completed_task() 
    elif opt ==5 :
        run.make_update_task()
    elif opt ==6 :
        run.make_complete_task()



    




    



    


        