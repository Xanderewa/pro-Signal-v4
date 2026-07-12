from src.strategies import StrategyEngine

class SignalManager:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.engine = StrategyEngine()

    def run(self):
        self.logger.info("Signal manager started")
