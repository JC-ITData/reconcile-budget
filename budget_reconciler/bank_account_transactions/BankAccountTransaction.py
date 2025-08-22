from budget_reconciler.utils import FileReader

class BankAccountTransaction:
  def __init__(self, config_file_name: str) -> None:
    self.config_file_name = config_file_name
    
    config_reader = FileReader.JsonFileReader()
    self.config = config_reader.read(file_path=config_file_name,file_desc='config file')


  def load_data_files(self, reload:bool=False) -> dict:
    data_file_reader = FileReader.CsvFileReader()
    schema_file_reader = FileReader.JsonFileReader()
    data_feeds = {}
    data_feeds_info = self.config['bank_data_feeds']
    # "skip_lines_until" : {"StringMatch" : "Date"}
    for feed_name in data_feeds_info.keys():
      # read json file
      feed_schema = schema_file_reader.read(file_path= data_feeds_info[feed_name]['schema_file'], file_desc=f"{feed_name} schema file")
      print(str(feed_schema.keys()))

      data_feeds[feed_name] = data_file_reader.read(
        data_feeds_info[feed_name]['data_files']
        , file_desc=f"{feed_name} bank data file"
        , delimiter=feed_schema['field_delimiter']
        , skip_until = feed_schema['skip_lines_until']
      )
    self.data_feeds = data_feeds
    return data_feeds


