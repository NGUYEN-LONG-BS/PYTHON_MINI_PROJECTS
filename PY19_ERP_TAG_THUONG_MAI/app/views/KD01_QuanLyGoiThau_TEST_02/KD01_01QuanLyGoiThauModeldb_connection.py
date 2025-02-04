import pyodbc
from utils import *

def create_connection():
    conn = f_utils_create_a_connection_string_to_SQL_Server()
    
    return conn