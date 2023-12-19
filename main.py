import json

class Entity:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Сущность: {self.name}'

class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    def __str__(self):
        return f'{self.name} работает в {self.company}'

# Создание экземпляров
cat = Entity('Сугроб')
employee = Employee('Петя', 'Foxford')

# Сериализация в JSON и запись в файл
data = {
  "Entity": {
    "name": cat.name
  },
  "Employee": {
    "name": employee.name,
    "company": employee.company
  }
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Вывод в консоль
print(cat)
print(employee)
