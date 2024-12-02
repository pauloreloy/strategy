from abc import ABC, abstractmethod
from classes.mapper import Mapper
from decorators.exceptions import exception
from typing import Dict, Any
import json
import xml.etree.ElementTree as ET

class ACTC(ABC):

    def __init__(self):
        self.headers = ""

    def generate_headers(self, actc_type: str) -> str:
        self.headers = f"headers do {actc_type}"
        return self.headers

    @staticmethod
    @exception
    def map_actc_data(actc_type: str, actc_proc: Dict[str, Any]) -> Dict[str, Any]:
        mapper = Mapper(actc_type)
        def map_actc_data(actc_proc: Dict[str, Any]) -> Dict[str, Any]:
            actc_data = {}
            for item in actc_proc:
                if (isinstance(actc_proc[item],list)):
                    g_key = mapper.map_item(item)
                    n_list = []
                    for sub_item in actc_proc[item]:
                        values = map_actc_data(sub_item)
                        n_list.append(values)
                    actc_data[g_key] = n_list
                elif (isinstance(actc_proc[item],dict)):
                    g_key = mapper.map_item(item)
                    values = map_actc_data(actc_proc[item])
                    actc_data[g_key] = values.copy()
                else:    
                    mapped = mapper.map_item(item)
                    actc_data[mapped] = actc_proc[item]
            return actc_data
        return map_actc_data(actc_proc)

    @abstractmethod
    def generate_xml(self, actc_proc: Dict[str, Any], actc_type: str) -> str:
        """
        Abstract method to generate XML for ACTC process.

        :param actc_proc: ACTC processed data
        :param actc_type: ACTC type
        :return: Generated XML
        """
        pass
