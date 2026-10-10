from abc import ABC,abstractmethod

class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class intern(employee):
    def calculate_salary(self):
        stipend = 10000
        print("INTERN STIPEND = ", stipend)

class full_time(employee):
    def calculate_salary(self):
      salary = 100000
      print("salary = ",salary)

class contract_employee(employee):
    def calculate_salary(self):
      rate = 1000
      hour = 7
      salary = hour * rate
      print("salary = ",salary)

i = intern()
f = full_time()
c = contract_employee()

i.calculate_salary()
f.calculate_salary()
c.calculate_salary()
