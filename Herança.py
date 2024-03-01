class Funcionarios:
    def __init__(self, nome, salario, matricula):
        self.nome = nome
        self.salario = salario
        self.matricula = matricula
    def showinfo(self):
        return f"Nome: {self.nome}" f"\nSalário: R${self.salario}" f"\nMatrícula: {self.matricula}"
class Prof (Funcionarios):
    def __init__(self, nome, salario, matricula, materia):
        super().__init__(nome, salario, matricula)
        self.materia = materia
    def showinfo(self):
        return super().showinfo() + f"\nMáteria: {self.materia}"
class Admin (Funcionarios):
    def __init__(self, nome, salario, matricula, cargo):
        super().__init__(nome, salario, matricula)
        self.cargo = cargo
    def showinfo(self):
        return super().showinfo() + f"\nCargo: {self.cargo}"
prof1 = Prof("Igor", 50, "Sp4569283", "Lab de Programação")
admin1 = Admin("Sheila", 76, "Sp2950495", "Assinstende")
print(prof1.showinfo())
print(admin1.showinfo())