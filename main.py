from enum import Enum
from typing import List
from tabulate import tabulate

globalConsts = {
  "bonusForExperience": 100,
  "noobSalary": 400,
  "bossSalary": 17000,
  "advancedSalary": 10000,
}

class Role(Enum):
  Boss = 1
  Noob = 2
  Advanced = 3

class Worker:
  def __init__(self, name: str, experience: float, baseSalary: int, role: Role):
    if (experience < 0):
      raise Exception(f"invalid experience value in constructor: {experience}. Property is expexted to be greater than 0")

    self.name = name
    self.experience = experience
    self.baseSalary = baseSalary
    self.baseSalary = baseSalary
    self.role = role

  @property
  def salary(self) -> float:
    return self.baseSalary + self.experience * globalConsts["bonusForExperience"]

class Boss(Worker):
  def __init__(self, name: str, experience: float):
    super(Boss, self).__init__(name, experience, globalConsts["bossSalary"], Role.Boss)

class Noob(Worker):
  def __init__(self, name: str, experience: float):
    super(Noob, self).__init__(name, experience, globalConsts["noobSalary"], Role.Noob)

class Advanced(Worker):
  def __init__(self, name: str, experience: float):
    super(Advanced, self).__init__(name, experience, globalConsts["advancedSalary"], Role.Boss)

class WorkerHandler:
  def __init__(self, workers: List[Worker] = None):
    self.workers = workers if workers is not None else []

  def addWorker(self, wroker: Worker):
    self.workers.append(wroker)

  def removeWorker(self, worker: Worker):
    if worker in self.workers:
      self.workers.remove(worker)

  def countSalaries(self):
    sum = 0

    for worker in self.workers:
      sum += worker.salary 

    return sum

  def wrokersToArray(self):
    workersArr = []

    for worker in self.workers:
      workersArr.append([worker.name, worker.role.name, worker.salary, worker.experience])

    return workersArr
    
  def logWorkers(self):
    print(tabulate(self.wrokersToArray(), headers=['Name', 'Role', 'Salary', 'Experience']))

wrokerHandler = WorkerHandler()
worker1 = Boss("Ihor", 5)
worker2 = Advanced("Artem", 4)
worker3 = Noob("Dima", 5)

wrokerHandler.addWorker(worker1)
wrokerHandler.addWorker(worker2)
wrokerHandler.addWorker(worker3)
wrokerHandler.logWorkers()
print(wrokerHandler.countSalaries())