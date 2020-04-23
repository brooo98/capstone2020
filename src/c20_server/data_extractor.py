from collections import namedtuple
import os

Data = namedtuple('Data', ['folder_name', 'file_name', 'contents'])


class MissingDataException(Exception):
    pass


class DataExtractor:

    @staticmethod
    def extract(list_of_data_dicts):
        ret = []

        for data_item in list_of_data_dicts:
            try:
                ret.append(Data(folder_name=data_item['folder_name'],
                                file_name=data_item['file_name'],
                                contents=data_item['data']))
            except TypeError:
                raise MissingDataException()
        return ret


    @staticmethod
    def save_files_disk(Data_list):
        
        for data in Data_list:
            
            directory = data.folder_name
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            detination = data.folder_name + '/' +data.file_name
            
            with open(detination,'w') as f:
                f.write(data.contents)


