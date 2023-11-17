import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        Path to yaml (str): Path from input.
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
        
    """
    try:
        with open(path_to_yaml) as yaml_f:
            content = yaml.safe_load(yaml_f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

# create directories function
@ensure_annotations
def create_dirs(path_to_dirs: list, verbose=True):
    """Create list of directories
    Args:
    Path_to_dirs (list): a list of directories to create
    ignore_log (bool, optional): ignore if multiple directories are to be created
    
    """
    
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory: {path}")
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dict to a json file
    
    Args:
        path (Path): Path to json file that we are going to write to.
        data (dict): Data to be saved inside the .json file.
    
    """
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at {path}")
    
@ensure_annotations
def load_json(path: Path):
    """loads a json file
    
    Args:
        path (Path): Path to json file that we are going to write to.
    
    returns:
        ConfigBox: Data as class attributes instead of dict
    """
    
    with open(path, 'r') as f:
        content = json.load(f)
    
    logger.info(f"json file lodaed from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save file as binary
    
    Args:
        data (Any): Data to be saved 
        path (Path): Path to save the data    
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"File saved at {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): File to be loaded from binary
    
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB
    Args:
        path (Path): Path to file that is to be measured
        
    Returns:
        str: size in KB
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"size: {size_in_kb} KB"

def decodeImage(img_string, filename):
    """Decodes img data into binary
    Args:
        path (Path): Path to binary image
    """
    
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(img_string))
        f.close()
        
def encodeImageIntoBase64(cropped_img_path):
    """Encodes cropped image back into base64
    Args:
        cropped_img_path (Path): Path to image to be binarized
    """
    
    with open(cropped_img_path, 'rb') as f:
        return base64.b64encode(f.read())