
import logging
import pandas as pd
from abc import ABC, abstractmethod
from budget_reconciler.utils import FileReader

class Transaction(ABC):
  def __init__(self, config_file_name: str) -> None:
    self.config_file_name = config_file_name
    config_reader = FileReader.JsonFileReader()
    self.config = config_reader.read(file_path=config_file_name, file_desc='config file')

  def load_data_files(self, data_feeds_key: str, reload: bool = False) -> dict:
    logging.info("Loading data files : " + data_feeds_key)
    data_file_reader = FileReader.CsvFileReader()
    schema_file_reader = FileReader.JsonFileReader()
    data_feeds = {}
    
    if data_feeds_key == 'budget_data_feed' :
      data_feeds_info = self.config
      feed_names = ['budget_data_feed',]
    else :
      data_feeds_info = self.config[data_feeds_key]
      feed_names = data_feeds_info.keys()
    
    for feed_name in feed_names:
      feed_schema = schema_file_reader.read(
        file_path=data_feeds_info[feed_name]['schema_file'],
        file_desc=f"{feed_name} schema file"
      )
      data_feeds[feed_name] = data_file_reader.read(
        data_feeds_info[feed_name]['data_files'],
        file_desc=f"{feed_name} data file",
        delimiter=feed_schema['field_delimiter'],
        skip_until=feed_schema['skip_lines_until']
      )
    self.data_feeds = data_feeds
    return data_feeds

