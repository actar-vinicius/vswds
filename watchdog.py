#!/usr/bin/python
import re
import os
import subprocess

def check_process(process):

  ps = subprocess.Popen("ps aux | grep coleta | grep -v grep", shell=True, stdout=subprocess.PIPE)
  process_list = ps.stdout.read()
  
  print "Procuro por: "+process+"\n"
  print "Na lista:\n"
  print process_list+"\n"
  
  for x in process_list.split(os.linesep):
    print "Procuro na linha: "+x
    if re.search(process.strip(), x):
      #se encontrou, returna True 
      print "Encontrei: "+process
      return True
  #Se nao encontrou o nome do processo, retorna False
  print "Nao encontrei: "+process
  return False

#Abre o arquivo contendo a lista de clientes e parametros (implementacao futura)
customers = open('customers', 'r')

for line in customers:
  if not check_process(line):
    #Executa o programa novamente seguindo o padrao nohup
    print "Foi preciso executar: "+line
    command = 'nohup python coleta-{0}.py  > /dev/null 2>&1 &'.format(line.strip()) 
    ss = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    ss.stdout.read()

customers.close()