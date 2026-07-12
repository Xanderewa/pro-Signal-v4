from config import Config
from src.signal_manager import SignalManager
from src.logger import BotLogger

def main():
    config = Config()
    logger = BotLogger()
    manager = SignalManager(config=config, logger=logger)
    manager.run()

if __name__ == "__main__":
    main().
