import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)

global results 
results = 0 
global tried 
tried = 0 
c = 0 

if not zipf:
    print('The zipped file\folder is not password protected! You can successfully open it!')
    
else:
    starttime = time.time()
    wordListFile = open('C:/Users/MBajw/OneDrive/Documents/Coding/notepad.txt','r',errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')
    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf-8').strip()
        c = c + 1
        print('Trying to decode password file by : {}'.format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd = password)
                print('Success! The password is: '+word)
                endtime = time.time()
                result = 1 
            break
        except:
            pass
        
    if (result == 0):
        duration = endtime - starttime
        print('Sorry, password was not found. A total of '+str(c)+'+possible combinations tried in '+str(duration)+'seconds.')
    else:
        duration = endtime - starttime
        print('Congratulations!! Password found after trying '+str(c)+'combinations in '+str(duration)+'seconds.')
                
