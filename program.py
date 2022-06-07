import os

print("========== START PROGRAM ==========")

#Configure the different functions

#Function for  OS
def create_folder():

    creation_path = str(input("What's the path ?"))  
    os.chdir(creation_path)

    folder_name = str(input("What's the name of the folder ?"))
    path = ("%s" % folder_name)

    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

def delete_folder():

    creation_path = str(input("What's the path ?"))
    os.chdir(creation_path)
    
    folder_name = str(input("What's the name of the folder ?"))
    path = ("%s" % folder_name)

    try:
        os.rmdir(path)
    except OSError:
        print("Can't delete the directory %s." % path)
    else:
        print("The directory %s has been successfully deleted." % path)

def wdyw_create():

    
    create_folder()

    #Asking if user want to create another directory
    answer_onemore = str(input('Do you want to create another directory ?'))
    
    while answer_onemore == 'yes':
        create_folder()
        answer_onemore = str(input('Do you want to create another directory ?'))

def wdyw_delete():
    
    delete_folder()

    #Asking if user want to delete another directory
    answer_onemore = str(input('Do you want to delete another directory ?'))
    
    while answer_onemore == 'yes':
        delete_folder()
        answer_onemore = str(input('Do you want to delete another directory ?'))

#Asking which function the user want to use (wdyw = why do you want)

answer_wdyw = str(input('What do you want to do ? create or delete ?'))

#Calling the right function 

if answer_wdyw == 'create':
    wdyw_create()

elif answer_wdyw == 'delete':
    wdyw_delete()

else:
    print('You didn\'t enter "create" or "delete", the script will close. Thanks for using our solution.')

print("Thanks for using our solution.")
print('========== END PROGRAM ==========')
