from budget_reconciler.utils import FileReader

class BankAccountTransaction:
  def __init__(self, config_file_name: str) -> None:
    self.config_file_name = config_file_name
    
    config_reader = FileReader.JsonFileReader()
    self.config = config_reader.read(file_path=config_file_name,file_desc='config file')


  def load_data_files(self, reload:bool=False) -> dict:
    data_file_reader = FileReader.CsvFileReader()
    data_feeds = {}
    data_feeds_info = self.config['data_feeds']
    for feed_name in data_feeds_info.keys():
      data_feeds[feed_name] = data_file_reader.read(data_feeds_info[feed_name]['data_files'], delimiter=data_feeds_info[feed_name]['data_file_delimiter'])
    self.data_feeds = data_feeds
    return data_feeds


