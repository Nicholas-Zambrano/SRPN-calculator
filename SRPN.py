# # To run Code:  python SRPN/srpn.py
# # To test code: python mark-code.py
# # to run fully: ~/SRPN-2022-NicoZAMB$ python SRPN/srpn.py

# Random numbers list
prov_r=[1804289383,521595368,35005211,1303455736,304089172,1540383426,1365180540,1967513926,2044897763,1102520059,783368690,1350490027,1025202362,1189641421,596516649,1649760492,719885386,424238335,1957747793,1714636915,1681692777,846930886,1804289383]

# Initialising an empty stack, setting the saturation limits and defining operators
stack = []
min_value = -2147483648
max_value = 2147483647
operators = ["+", "-", "*", "/", "%", "^"]


# Function to check if the result after operations lies within the saturation limits and appends to the stack
def check_res(result): 
  if result > max_value: 
    stack.append(max_value)
  elif result < min_value:
    stack.append(min_value)
  else:
    stack.append(int(result))

    
# Function to check the user input is within saturation limits and if there is space to append in the stack.
# Else it will print stack overflow.
def numbers_check(command):  
  if len(stack)<23:
    if int(command)>max_value:
      stack.append(max_value)
    elif int(command)<min_value:
      stack.append(min_value)
    else:
      stack.append(int(command))
  else:
    print("Stack overflow.")

# Operation function to perform calculations.
def operation_calc(command):

# If there is more than one number in the stack, we pop the last two numbers  
  if len(stack) > 1:
    num1 = stack.pop() 
    num2 = stack.pop()     

# Deals with operations and appends each calculation within the saturation limits        
    if command=="+":      
      result=num1+num2
      check_res(result) 
      
    elif command=="-":
      result=num2-num1
      check_res(result)
      
    elif command=="*":
      result=num1*num2
      check_res(result)
      
    elif command=="%":
      result=num2%num1
      check_res(result)

# If num1 is zero when dividing, it will print 'Divide by 0.'
    elif command=="/":
      if num1 != 0: 
        result=num2/num1
        check_res(result)        
      else:
        print("Divide by 0.") 
    
# If num1 is less than 0 when the '^' operator is called, then we print 'Negative power'.    
    elif command=="^":
      if num1<0:
        stack.append(num2)
        stack.append(num1)
        print("Negative power.") 
      else:
        result=pow(num2,num1)
        check_res(result)        
# If there are less than two numbers, we execute the 'else' statement
  else:
    print("Stack underflow.")      

            
# Main body   
def process_command(command):
  
# If user input is within operators list, then we call the operation_calc function
  
  if command in operators:
    operation_calc(command)
  
# If user does not input spaces between the hash and characters, then function will print 'Unrecognised operator/operand'
  
  elif "#" in command:      
    print("Unrecognised operator or operand",'"'+"#" + '"'+ ".")  

# Once user inputs a '#', then we iterate through each character specifying unrecognised operator/operand
    
    for z in range(0,len(command)):
      if command[z] not in operators and not command[z].isdecimal or command[z].isalpha() :
              
        print("Unrecognised operator or operand",'"' + command[z].strip()+'".')
    print("Unrecognised operator or operand",'"'+"#" + '"'+ ".")  

    
# If user inputs 'r', we run a while loop to pop and append each 'r' value to the stack from the prov_r list
# If there is no space in the stack, we print stack overflow  
  
  elif command == "r":
    while True:      
      if command == "r" :
        if len(stack)<23:
          stack.append(prov_r.pop())
          break
        else:
          print("Stack overflow.")
          break

# If user inputs '=' and there are numbers in the stack, we print the top value.
# Else we print 'stack empty'.          
          
  elif command == "=":  
    if len(stack) > 0:
        print(stack[-1])          
    else:
      if len(stack) == 0:
        print("stack empty", sep='\n')
          
# If user inputs 'd' and the length of the stack is greater than zero, then we iterate and print the stack for each 'd'.
# Else, we print the minimum value
        
  elif "d" in command:             
     if len(stack)>0: 
       for w in range(len(command)):  
         if command[w] == "d":
           print(*stack, sep="\n")
     else:
       for w in range(len(command)):
         if command[w]=="d":  
           print(min_value)

# If user input is not in the operators list,is not a number or are letters. Then we print unrecognised operator/operand
           
  elif command not in operators and not command.isdecimal or command.isalpha():
    for z in range(len(command)):
      print("Unrecognised operator or operand",'"' + command[z].strip()+'".')      

# If user inputs integers, we call numbers_check function 
  else:    
    numbers_check(command) 
    

# We take the user input in cmd, split this and process it through the main body function
# We use a for loop to iterate through each element within the input.
# If user inputs '#', then we break to ignore all the elements which follows after a space
    
if __name__ == "__main__":
  while True:
    try:
      cmd = input()

      cmd_splitted  = cmd.split() 
      
      for i in range(0, len(cmd_splitted)): 
        if cmd_splitted[i] =="#":         
          break                       
        
        process_command(cmd_splitted[i])      

    except EOFError:
      exit()

