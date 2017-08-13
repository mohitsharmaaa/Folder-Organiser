# Folder/Drive Organiser program in Python
# Cleans up messy folders and create folders according to file types

import os

Images=['.png','.jpg','.tiff','.gif','.bmp','.ppm','.pgm','.pbm','.pnm','.jpeg','.heif','.bpg','.img','.ico']
Documents=['.doc','.txt','.pdf','.xls','.docx','.html','.htm','.odt','.xlsx','.ppt','.pptx']
Videos=['.mp4','.mkv','.webm','.flv','.vob',',ogv','.ogg','.drc','.gifv','.mng','.wmv','.mov','.qt','.avi','.yuv','.rm','.asf','.amv','.m4v','.m4p','.3gp']
Audios=['.mp3','.raw']
Zip_Files=['.7z','.zip','.rar']

final_path=os.getcwd()

folders_list=['Images','Documents','Videos','Audios','Zip_Files','Others']



# Handle Dupicate Names and move files with respective folders  
def duplicate_name_handle(old_path,file_name,folder_name):
    file_extension="."+file_name.split(".")[-1]
    try:
        try:
            os.rename(old_path,final_path+"/"+folder_name+"/"+file_name)
        except(FileNotFoundError):
            try:
                os.mkdir(final_path+"/"+folder_name)
                os.rename(old_path,final_path+"/"+folder_name+"/"+file_name)
            except(FileExistsError):
                c=1
                while(True):
                    try:
                        if(file_name.count("(")>0):
                            file_name=file_name.split("(")[0]
                        else:    
                            file_name="".join(file_name.split(".")[:-1])
                        file_name=file_name+"("+str(c)+")"+file_extension
                        os.rename(old_path,final_path+"/"+folder_name+"/"+file_name)
                        break
                    except:
                        c+=1
        except(FileExistsError):
            
            c=1
            while(True):
                try:
                    if(file_name.count("(")>0):
                        file_name=file_name.split("(")[0]
                    else:    
                        file_name="".join(file_name.split(".")[:-1])
                    file_name=file_name+"("+str(c)+")"+file_extension
                    os.rename(old_path,final_path+"/"+folder_name+"/"+file_name)
                    break
                except:
                    c+=1 
    except:
        os.mkdir(final_path+"/"+folder_name)
        os.rename(old_path,final_path+"/"+folder_name+"/"+file_name)
                        
#Uses File Extension to categorize files
def move_file(old_path,file_name):
    try:
        file_extension=("."+file_name.split(".")[-1]).lower()
        #list_of_files=os.listdir()
        if file_extension in Images:
            duplicate_name_handle(old_path,file_name,"Images")
            
        elif file_extension in Documents:
            duplicate_name_handle(old_path,file_name,"Documents")
           
        elif file_extension in Audios:
            duplicate_name_handle(old_path,file_name,"Audios")
            
        elif file_extension in Videos:
            duplicate_name_handle(old_path,file_name,"Videos")
            
        elif file_extension in Zip_Files:
            duplicate_name_handle(old_path,file_name,"Zip_Files")
            
        else:
            if file_name!="folder_organiser.py":
                duplicate_name_handle(old_path,file_name,"Others")
                
    except:
        print("Error"+file_name)                

#Explore the directory            
#seperate folders and files in current directory 

def file_explorer(current_path):
    for path,folders,file_list in os.walk(current_path, topdown=False):
        for file_name in file_list:
            move_file(path+"/"+file_name,file_name)
        try:
            os.rmdir(path)
        except:
            print(path.split("/")[-1]+" created")
    
    return "\n\nThere you go.. It's Done :)"        
                            
def start_from_here():                            
    print("-"*80)
    print(" "*30+" FOLDER ORGANISER "+" "*50)
    print(" "*45+" by github/mohitsharmaaa")
    print("-"*80+"\n\n")
    print("Files are organising.... wait for completion message\n\n")           
    msg=file_explorer(os.getcwd())
    print(msg)
    
start_from_here()    
k=input()