from registration_form import DisplayRegistrationForm
import os 
from main_prompt2 import mainPrompt 

def checkKey()->bool:
    
    current_dir = os.getcwd()
    keyFileName = "key.txt"
    
    #check if key_file exists
    if not os.path.isfile(r'{0}\{1}'.format(current_dir, keyFileName)) :
        CreateKeyFile = open("key.txt","w")
        CreateKeyFile.close()
    
    keyFile_toCheck = open(r'key.txt','r')
    key = keyFile_toCheck.readline()
    if key == "true":
        return True 
    else:
        return False 
    

def main():
    """Process of execution
    1. settings of config data
    2. normal run"""

    #Check if registration is succesfull
    RegistrationDone = checkKey()
    if not RegistrationDone:
        DisplayRegistrationForm()
        mainPrompt()
    
    #display main prompt
    mainPrompt()
    
if __name__=="__main__":
    main()
