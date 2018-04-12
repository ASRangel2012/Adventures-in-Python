#lab 10
#fileName:file_reader_angelSR2.py

fileName = 'pi_digits.*txt'
with open(fileName) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())


    
