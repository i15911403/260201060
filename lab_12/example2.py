class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def get_name(self):
    return self.name

  def set_name(self,name):
    self.name = name

  def get_salary(self):
    return self.salary

  def set_salary(self,salary):
    if salary > 0 :
      self.salary = salary


  def show_inf(self):
    print("Name:",self.name)
    print("Salary:",self.salary)

class Company:
  def __init__(self):
    self.employee_list = []
  
  def get_employee(self):
    return self.employee_list
  
  def set_employee(self,current_list):
    if type(current_list) == list:
      self.employee_list = current_list
  
  def add_employee(self,new_employee):
    if isinstance(new_employee,Employee):
      self.employee_list.append(new_employee)
  
  def average_salary(self):
    total_salary = 0
    for i in self.employee_list:
      total_salary += i.get_salary()
    return total_salary / len(self.employee_list)
  
  def shows_employee(self):
    for i in self.employee_list:
      print("Name:",i.get_name())
      print("Salary:",i.get_salary())

c = Company()
e1 = Employee(name="Onur",salary=500)
e2 = Employee(name="Altuğ",salary=400)
e3 = Employee(name="Can",salary=300)

c.add_employee(new_employee=e1)
c.add_employee(new_employee=e2)
c.add_employee(new_employee=e3)
c.shows_employee()