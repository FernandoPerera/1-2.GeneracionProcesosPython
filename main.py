import platform
import sys
import os

from time import sleep

system = platform.system()

def father() :
    print('\n\t-------------------------------------------------')
    numChildProcesses = int(input('\tHola usuario, introduce cuantos procesos ejecutar\n\t'))
    
    executables = {
        'linux' : os.fork()
    }
    
    contador = 0
    
    while (contador < numChildProcesses) :
        
        contador += 1
        
        newPid = [executables[sys.platform]]
        
        if newPid == 0 :        
            children()
        else :
            fatherPid = os.getpid()
            childrenPid = newPid
            
            print('PID del padre : %s, PID del hijo : %s\n' % (fatherPid, childrenPid))
        
def children() :
    print('\n\t········ | Hijo con PID %d | ········' % os.getpid())
    sleep(5)
    print('\n\t········ | PID %d ha muerto :( | ········' % os.getpid())

    os._exit(0)
        
father()