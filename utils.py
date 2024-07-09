import box
from box import ConfigBox
from pathlib import Path
import yaml

def read_Yml_file(ymal_file_path:Path)->ConfigBox:

    try:
        with open (ymal_file_path) as file:
            content = yaml.safe_load(file)
            return ConfigBox(content)
        
    except yaml.YAMLError as err:

        print(err)
