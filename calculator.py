import os
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def divide(a,b):
  return a/b
def multiply(a,b):
  return a*b
operations_dictionery={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
num1=float(input("Enter the first number: "))
for i in operations_dictionery:
  print(i)          #to print all the keys.
continue_operation=True
while continue_operation:
    operation_symbol=input("Enter the operation symbol: ")
    num2=float(input("Enter the second number: "))
    calculation_function=operations_dictionery[operation_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    should_continue=input(f"Enter 'y' to continue the calculation with {answer} or 'n' to start a new calculation or 'x' to exit:").lower()
    if should_continue=='y':
      num1=answer 
    elif should_continue=='n':
      os.system('cls' if os.name == 'nt' else 'clear')
      num1=int(input("Enter the first number: "))
      for i in operations_dictionery:
        print(i) 
      
    elif  should_continue=='x':
      continue_operation=False
      print("your calculations are over")
