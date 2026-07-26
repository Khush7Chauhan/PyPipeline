from .base import FileProcessor
from .csv_proc import CSVProcessor
from .json_proc import JSONProcessor
from .txt_proc import TXTProcessor

__all__ = ["FileProcessor", "CSVProcessor", "JSONProcessor", "TXTProcessor"]