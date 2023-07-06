from lark import Transformer
from typing import Dict, Any, List, Union

class CarTransformer(Transformer):
    def start(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        return items[0]

    def toyota(self, items: List[Dict[str, str]]) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        return {"data": items}

    def toyota_brand(self, items: List[str]) -> Dict[str, str]:
        return {"brand": items[0].value}

    def toyota_model(self, items: List[str]) -> Dict[str, str]:
        return {"model": items[0].value}

    def honda(self, items: List[Dict[str, str]]) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        return {"data": items}

    def honda_brand(self, items: List[str]) -> Dict[str, str]:
        return {"brand": items[0].value}

    def honda_model(self, items: List[str]) -> Dict[str, str]:
        return {"model": items[0].value}

    def color(self, items: List[str]) -> Dict[str, str]:
        return {"color": items[0].value}
