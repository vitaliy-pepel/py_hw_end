import os
import logging
from collections import namedtuple

# Настройка логгера
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Определение структуры namedtuple для хранения информации о файлах и каталогах
File = namedtuple('File', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_file_info(directory_path):
    try:
        files_info = []
        parent_dir = os.path.basename(os.path.normpath(directory_path))
        
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            if os.path.isdir(full_path):
                files_info.append(File(name=item, extension='', is_dir=True, parent_dir=parent_dir))
            else:
                name, extension = os.path.splitext(item)
                files_info.append(File(name=name, extension=extension, is_dir=False, parent_dir=parent_dir))
        
        with open('file_info.txt', 'w') as file:
            for file_info in files_info:
                file.write(f"Name: {file_info.name}, Extension: {file_info.extension}, Is Directory: {file_info.is_dir}, Parent Directory: {file_info.parent_dir}\n")
        
        logging.info(f"Information collected successfully for directory: {directory_path}")
    
    except Exception as e:
        logging.error(f"Error occurred while collecting information for directory: {directory_path}. Error message: {str(e)}")

if __name__ == '__main__':
    directory_path = input("Enter the directory path: ")
    get_file_info(directory_path)