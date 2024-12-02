from classes.strategies.actc103 import ACTC103

strategies = {
    "ACTC103": ACTC103
}

class ACTCContext:
    
    def __init__(self, strategy, actc_type: str):
        self.strategy = strategy
        self.actc_type = actc_type
    
    def set_strategy(self, strategy, actc_type: str):
        self.strategy = strategy
        self.actc_type = actc_type

    def generate_xml(self, actc_proc: dict) -> str:
        return self.strategy.generate_xml(actc_proc, self.actc_type)

def actc_strategy(func):
    def wrapper(actc_type, *args, **kwargs):
        actc_context = ACTCContext(strategies[actc_type], actc_type)
        return actc_context
    return wrapper
