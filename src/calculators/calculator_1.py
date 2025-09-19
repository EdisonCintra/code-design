from typing import Dict
from flask import request as FlaskRequest

class Calculator1():

    def calculate(self, request : FlaskRequest):
        body = request.json

    def __validat_body(self, body : Dict):
        pass 