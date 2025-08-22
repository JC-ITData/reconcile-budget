import json
import logging
import pandas as pd
from abc import ABC, abstractmethod
import os
from pathlib import Path



class FileReader(ABC):

    def read(self, file_path: str, file_desc: str = '', **kwargs):

        file_desc = file_desc if file_desc else file_path.split('/')[-1]
        results_list = []

        path_obj = Path(file_path)
        if not(path_obj.exists()):
            message = f"Error: {file_desc} was not found. {str(path_obj)}"
            logging.error(message)
            raise FileNotFoundError(message)
        
        if (path_obj.is_dir()):
            list_files = [str(item) for item in path_obj.glob('*')]
        else :
            list_files = [ str(path_obj), ]        

        for file_name in list_files:
            try:
                results_list.append(self._read_file(file_name, **kwargs))
            except FileNotFoundError:
                logging.error(f"Error: {file_desc} was not found.")
                raise
            except IOError as e:
                logging.error(f"Error opening or reading {file_desc}: {e}")
                raise
            except Exception as e:
                logging.error(f"An unexpected error occurred while reading {file_desc}: {e}")
                raise
            finally:
                logging.info(f"{file_desc} read.")

        return_data = self._combine_read_files(results_list)
        return return_data

    @abstractmethod
    def _read_file(self, file_path: str, **kwargs):
        pass

    @abstractmethod
    def _combine_read_files(self, results_list):
        pass

class JsonFileReader(FileReader):
    def _read_file(self, file_path: str) -> dict :
        try :
            with open(file_path, 'r') as json_file:
                return_hash = json.load(json_file)
        except Exception as e:
            logging.error(f"Error reading json file into hash : {file_path}\n{e}")
            raise
        return return_hash
    
    def _combine_read_files(self,results_list: list[dict]) -> dict :
        return_dict = {}
        for dict_item in results_list:
            return_dict = {**return_dict, **dict_item}
        return return_dict

class CsvFileReader(FileReader):
    def _read_file(self, file_path: str, delimiter: str, skip_until: dict = None) -> pd.DataFrame:
        
        # setting for do not skip any lines:
        # "skip_lines_until" : {"LineNumber" : -1}

        if skip_until != None :
            if 'LineNumber' in skip_until.keys():
                line_start_num = skip_until['LineNumber']
            elif 'StringMatch' in skip_until.keys():
                search_str = skip_until['StringMatch']
                with open(file_path,'r') as file1:
                    for i,line in enumerate(file1):
                        if line.startswith(search_str):
                            line_start_num = i
            else :
                raise "Skip until setting not recognized. " + str(skip_until)
        else :
            line_start_num = -1

        try :
            if line_start_num == -1:
                return_df = pd.read_csv(file_path, delimiter=delimiter)
            else:
                return_df = pd.read_csv(file_path, delimiter=delimiter, skiprows=line_start_num)
        except Exception as e:
            logging.error(f"Error reading csv into pandas dataframe : {file_path}\n{e}")
            raise
        return return_df
    
    def _combine_read_files(self,results_list: list[pd.DataFrame]) -> pd.DataFrame:
        return_df = pd.DataFrame()
        for df in results_list :
            return_df = pd.concat([return_df,df],ignore_index=True)
        return return_df
