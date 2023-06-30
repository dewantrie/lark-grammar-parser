import logging

from car_transformer import CarTransformer
from lark import Lark, logger
from typing import Dict, Any

logger.setLevel(logging.WARN)

class EntityExtraction:
    def __init__(self):
        self.parser = Lark.open('car.lark')
        self.transformer = CarTransformer()

    def doc(self, sentence: str) -> Dict[str, Any]:
        tree = self.parser.parse(sentence)
        return self.transformer.transform(tree)
