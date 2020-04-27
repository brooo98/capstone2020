from c20_server.data_extractor import DataExtractor, MissingDataException
from c20_server.in_progress import InProgress
import os




def get_document_id(file_name):
    """
       return document id from file name
    """
    
    document_id = file_name.split('.')[1]
    return document_id
    
def get_file_name(file_path):
    """
        return file name by file path
    """
    split_path = file_path.split('/')
    file_name = split_path[len(split_path) - 1]
    return file_name

def create_new_directory(path):
    """
        create new directory
    """
    if not os.path.exists(path):
        os.makedirs(path)

def save_single_file(current_path, destination):
    pass
    
    
def save_all_files(file_list, path_to_file_list, destination):
    """
    save all files
    """
    for file in file_list:
        file_path = path_to_file_list + file
        save_single_file_locally(file_path, destination)



def check_update_file(file, json_data, tmp_dir_path):
    pass
   
def save_doc_process(job_manager, json_data,destination):
    """
    save to disk process function
    """
    # Verifies that a given job is in the "progress" queue exists
    # job_in_progress function does not exists/created yet in_progress/job_manager file !!!
    
    if job_manager.job_in_progress(json_data['job_id']):
        temp_directory = tempfile.mkdtemp()
        tmp_dir_path = str(temp_directory + '/')
        
        file_list, tmp_dir_path = DataExtractor.extractor(json_data)
        
        check_update = False
        
        for file in file_list:
            check_job_update = check_update_file(file, json_data, tmp_dir_path)
            if check_job_update is True:
                # function not exists/created yet in job manager!!!
                job_manager.update(json_data['job_id'])
                check_update = True
                break
        if check_update is False:
            save_all_files(file_list, tmp_dir_path, destination)
            # this function unsign from progress not exists/created yet in progress !!!!
            InProgress.remove_from_progress(json_data)
                