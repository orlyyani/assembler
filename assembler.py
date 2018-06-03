#!/usr/bin/python

with open('command.txt', 'r') as f:
  x = f.read().splitlines()

machine_code = ''

def SetInstructionCode(code):
  return (bin(code)[2:].zfill(5))

def SetToRegister(reg):
  return (bin(reg)[2:].zfill(2))

def SetToMemoryAddress(address):
  return (bin(address)[2:].zfill(13))

def ZeroChecker(type):
  if type == 'IsZeroGoTo':
    return 6
  elif type == 'NotZeroGoTo':
    return 7
  elif type == 'GTZeroGoTo':
    return 8
  elif type == 'LTZeroGoTo':
    return 9
  elif type == 'GTEZeroGoTo':
    return 10
  elif type == 'LTEZeroGoTo':
    return 11

def OperandChecker(type):
  if type == 'Add':
    return 12
  elif type == 'Sub':
    return 13
  elif type == 'Mult':
    return 14
  
def SetMachineCode(ins, reg, mem):
  global machine_code
  print(ins + ' ' + reg + ' ' + mem)
  machine_code += ins+reg+mem
  # print(machine_code + '\n')

for i in x:
  operand = i.split('(')
  if (len(operand) > 1):
    parameter = operand[1].split(',')

  if(operand[0] == 'Forward'):
    SetMachineCode(SetInstructionCode(1), SetToRegister(0), SetToMemoryAddress(0))
  elif(operand[0] == 'LeftTurn'):
    SetMachineCode(SetInstructionCode(2), SetToRegister(0), SetToMemoryAddress(0))
  elif(operand[0] == 'RightTurn'):
    SetMachineCode(SetInstructionCode(3), SetToRegister(0), SetToMemoryAddress(0))
  elif(operand[0] == 'HasValue'):
    mem = int(parameter[0].strip(')'))
    SetMachineCode(SetInstructionCode(4), SetToRegister(0), SetToMemoryAddress(mem))
  elif(operand[0] == 'GoTo'):
    mem = int(parameter[0].strip(')'))    
    SetMachineCode(SetInstructionCode(5), SetToRegister(0), SetToMemoryAddress(mem))
  elif(operand[0] == 'IsZeroGoTo' or operand[0] == 'NotZeroGoTo' or operand[0] == 'GTZeroGoTo' or operand[0] == 'LTZeroGoTo' or operand[0] == 'GTEZeroGoTo' or operand[0] == 'LTEZeroGoTo'):
    reg = int(parameter[0].strip(')'))
    mem = int(parameter[1].strip(')'))
    code = ZeroChecker(operand[0])
    SetMachineCode(SetInstructionCode(code), SetToRegister(reg), SetToMemoryAddress(mem))
  elif(operand[0] == 'Add' or operand[0] == 'Sub' or operand[0] == 'Mult'):
    reg = int(parameter[0].strip(')'))
    mem1 = int(parameter[1].strip(')'))
    mem2 = int(parameter[2].strip(')'))
    code = OperandChecker(operand[0])
    mem = SetToRegister(mem1) + SetToRegister(mem2) + bin(0)[2:].zfill(9)
    SetMachineCode(SetInstructionCode(code), SetToRegister(reg), mem)
  elif(operand[0] == 'ReadMem' or operand[0] == 'WriteMem'):
    reg = int(parameter[0].strip(')'))
    mem = int(parameter[1].strip(')'))
    if(operand[0] == 'ReadMem'):
      code = 15
    else:
      code = 16
    SetMachineCode(SetInstructionCode(code), SetToRegister(reg), SetToMemoryAddress(mem))
  elif(operand[0] == 'SetReg'):
    reg = int(parameter[0].strip(')'))
    mem = int(parameter[1].strip(')'))    
    SetMachineCode(SetInstructionCode(17), SetToRegister(reg), SetToMemoryAddress(mem))
  else:
    print('Invalid Syntax "', operand[0], '"')
    