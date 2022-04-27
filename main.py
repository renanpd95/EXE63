import os

nome = str(input("Digite nome do funcionario: "))
sal = float(input("Digite o sálario do funcionario: R$"))

os.system('clear')

if(sal < 3636 ):
  
  calc1 = 1.50 * sal
  print("Nome: ",nome)
  print("Salario atual: R$",sal)
  print(f"Salario reajustado: R${calc1:.2f}")
  
elif(sal >= 3636 and sal < 12120):
  
  calc2 = 1.20 * sal
  print("Nome: ",nome)
  print("Salario atual: R$",sal)
  print(f"Salario reajustado: R${calc2:.2f}")
  
elif(sal >= 12120 and sal < 24240):
  
  calc3 = 1.15 * sal
  print("Nome: ",nome)
  print("Salario atual: R$",sal)
  print(f"Salario reajustado: R${calc3:.2f}")
  
elif(sal >= 24240 ):
  
  calc4 = 1.10 * sal
  print("Nome: ",nome)
  print("Salario atual: R$",sal)
  print(f"Salario reajustado: R${calc4:.2f}")
  