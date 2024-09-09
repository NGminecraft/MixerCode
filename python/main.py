import logging
from communication import Comms
from utilClasses.cmd import CMD
from statusCache import Status
from terminal import Terminal

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
    logger.debug("Initializing")
    communicationClass = Comms()
    logger.info("Initialized Communication Class")
    communicationClass.registerListener(reportInput, CMD("meters/01"))
    storageClass = Status(communicationClass.registerListener, 3)
    terminal = Terminal(storageClass)
    while True:
        terminal.update()
    print()
    
    

if __name__ == "__main__":
    main()