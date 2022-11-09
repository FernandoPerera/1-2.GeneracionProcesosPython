import os

from time import sleep

def father() :
    
    try :
        
        print('\n\t-------------------------------------------------')
        numChildProcesses = int(input('\tHola usuario, introduce cuantos procesos ejecutar\n\t'))
            
        contador = 0
        
        while (contador < numChildProcesses) :
            
            newPid = os.fork()
            
            if newPid == 0 :        
                children()
            else :
                fatherPid = os.getpid()
                childrenPid = newPid
                
                print('PID del padre : %s, PID del hijo : %s\n' % (fatherPid, childrenPid))
                
            contador += 1
    
    except :
        
        print('\n\t*****************************************************')
        print('\tERROR : El dato introducido debe ser un número entero')
        print('\t*****************************************************')
        
        
def children() :
    print('\t········ | Hijo con PID %d | ········\n' % os.getpid())
    sleep(5)
    print('\n\t········ | PID %d ha muerto :( | ········' % os.getpid())

    os._exit(0)
        
father()