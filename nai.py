import pandas as pd
import numpy as np
import datetime

class nai():
    now = datetime.datetime.now()
    def read_csv(path):
        return pd.read_csv(path)

    def get_date():
        return nai.now.strftime("%Y-%m-%d")
    
    def date_diff():
        pass
        
    def find_null():
        pass
    
    def get_sql():
        pass
    
    def inner_join():
        pass
    
    def left_join():
        pass
    
    def union():
        pass
    
    def rbind():
        pass
    
    def cbind():
        pass
    
    def run_reg():
        pass
    
    def run_class():
        pass
    
