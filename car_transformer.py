from lark import Transformer
from typing import Dict, Any, List, Union

class CarTransformer(Transformer):
    def start(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        return items[0]

    def toyota(self, items: List[Dict[str, str]]) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        return {"data": items}

    def TOYOTA_BRAND(self, items: List[str]) -> Dict[str, str]:
        return {"brand": items.value}

    def TOYOTA_MODEL(self, items: List[str]) -> Dict[str, str]:
        return {"model": items.value}
    
    def TOYOTA_UNK(self, items: List[str]) -> Dict[str, str]:
        return {"unknown": items.value}

    def honda(self, items: List[Dict[str, str]]) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        return {"data": items}

    def HONDA_BRAND(self, items: List[str]) -> Dict[str, str]:
        return {"brand": items.value}

    def HONDA_MODEL(self, items: List[str]) -> Dict[str, str]:
        return {"model": items.value}
    
    def HONDA_UNK(self, items: List[str]) -> Dict[str, str]:
        return {"unknown": items.value}

    def COLOR(self, items: List[str]) -> Dict[str, str]:
        return {"color": items.value}
    
    
