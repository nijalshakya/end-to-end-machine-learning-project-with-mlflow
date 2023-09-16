import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_dtypes = list(data.dtypes)

            all_schema = self.config.all_schema.keys()
            all_schema = self.config.all_schema.values()

            
            for col in all_cols:
                for dtype in all_dtypes:
                    if col and dtype not in all_schema:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else:
                        validation_status = True
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
