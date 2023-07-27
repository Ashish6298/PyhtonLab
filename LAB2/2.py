class Job:
     

    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

def schedulejobs(jobs, T):
    profit=0
    slot=[-1]*T
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        for j in reversed(range(min(T, job.deadline))):
            if slot[j]==-1:
                slot[j]=job.taskId
                profit += job.profit
                break 
    print("The scheduled jobs are",list(filter(lambda x: x !=-1,slot)))
    print("The total profit earned is",profit) 

if __name__ =='__main__':   
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        taskId = input("Enter task ID for job {}: ".format(i+1))
        deadline = int(input("Enter deadline for job {}: ".format(i+1)))
        profit = int(input("Enter profit for job {}: ".format(i+1)))
        jobs.append(Job(taskId, deadline, profit))
    T = int(input("Enter the total time: "))
    schedulejobs(jobs, T)
    
    # OUTPUT
    
# Enter the number of jobs: 6
# Enter task ID for job 1: 1
# Enter deadline for job 1: 2
# Enter profit for job 1: 200
# Enter task ID for job 2: 3
# Enter deadline for job 2: 3
# Enter profit for job 2: 100
# Enter task ID for job 3: 3
# Enter deadline for job 3: 2
# Enter profit for job 3: 30
# Enter task ID for job 4: 4
# Enter deadline for job 4: 3
# Enter profit for job 4: 100
# Enter task ID for job 5: 5
# Enter deadline for job 5: 4
# Enter profit for job 5: 50
# Enter task ID for job 6: 6
# Enter deadline for job 6: 1
# Enter profit for job 6: 30
# Enter the total time: 4
# The scheduled jobs are ['4', '1', '3', '5']
# The total profit earned is 450