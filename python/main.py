import logging
from time import sleep
from communication import Comms
from utilClasses.cmd import CMD
from statusCache import Status
from terminal import Terminal
from config import get_config

def resetLogger():
    for i in ["debugLog.log", "log.log"]:
        with open(i, "w") as f:
            f.write("")

def setupLogger():
    logger = logging.getLogger("logger.main")
    logger.setLevel(logging.DEBUG)
    
    log_format = logging.Formatter('(%(name)s) %(asctime)s --[%(levelname)s]-- %(message)s')
    debugConfig = logging.FileHandler("debugLog.log")
    debugConfig.setLevel(logging.DEBUG)
    debugConfig.setFormatter(log_format)
    
    normalLogger = logging.StreamHandler()
    normalLogger.setLevel(logging.INFO)
    normalLogger.setFormatter(log_format)
    
    normalFile = logging.FileHandler("log.log")
    normalFile.setLevel(logging.INFO)
    normalFile.setFormatter(log_format)
    
    logger.addHandler(debugConfig)
    logger.addHandler(normalLogger)
    logger.addHandler(normalFile)
    return logger

def reportInput(address, *args):
    logging.getLogger(logging.getLogger("logger.main")).debug(f"{address} {args}")

def main():
    resetLogger()
    logger = setupLogger()
    logger.debug("Initialized Logger")
    logger.debug("Initializing config")
    configClass = get_config()
    logger.debug("Config Initialized, Initializing Communications")
    communicationClass = Comms(configClass)
    communicationClass.registerListener(reportInput, CMD("/*"))
    communicationClass.registerListener(reportInput, CMD("/xinfo"))
    communicationClass.sendMessage("/xinfo")
    logger.info("Initialized Communication Class, Starting on storage class")
    storageClass = Status(communicationClass)
    terminal = Terminal(storageClass, configClass)
    while True:
        """
        try:
            data, addr = communicationClass.get_socket().recvfrom(1024)
            if data:
                logger.debug(f"got {data} from {addr}")
        except BlockingIOError:
            pass
            """ 
        terminal.update()
        sleep(0.1)
        
    print()
    
    
try:
    if __name__ == "__main__":
        main()
finally:
    print("\033[?1049l")
