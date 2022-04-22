from logging import Filter
from pprint import pprint

class ManagementFilter(Filter):
    '''Class to filter out all log info created by the SQL Database'''

    def filter(self,record):
        if(hasattr(record,'funcName')) and record.funcName =='execute':
            return False
        return  True

