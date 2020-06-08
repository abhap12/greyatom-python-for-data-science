# --------------
#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file=open(path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    #Closing of the file
    file.close()
    return sentence
    #Returning the first line of the file
    
    

#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file
print(sample_message)
#Function to fuse message

def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    return str(quotient)
    
    #Returning the quotient in string format
    
#Calling the function to read file  
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
#Calling the function to read file
print(message_1,message_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)
#Printing the secret message 

#Function to substitute the message
def substitute_msg(message_c):
    if message_c == 'Red':
        sub ='Army General'
    elif message_c == 'Green':
        sub ='Data Scientist' 
    else:
        sub = 'Marine Biologist'
    
    #If-else to compare the contents of the file
    return sub
    
    #Returning the substitute of the message
    
    

#Calling the function to read file
message_3=read_file(file_path_3)
print(message_3)

#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)
#Printing the secret message

#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list=[i for i in a_list if i not in b_list]
    final_msg=" ".join(c_list)
    return final_msg
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)

#Calling the function to read file
print(message_4,message_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

def extract_msg(message_f):
    a_list=message_f.split()
    even_word = lambda x: len(x)%2==0
    b_list=filter(even_word,a_list)
    final_msg=" ".join(b_list)
    return final_msg

message_6=read_file(file_path_6)
print(message_6)
secret_msg_4=extract_msg(message_6)
print(secret_msg_4)
message_parts=['you are now','1', 'step closer to become', 'Data Scientist']
secret_msg=" ".join(message_parts)
def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()

final_path= user_data_dir + '/secret_message.txt'
write_file(secret_msg,final_path)
print(secret_msg)











