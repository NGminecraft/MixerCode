import logging


class CommandHandler:
    def __init__(self, config, communicationClass):
        self.communicationClass = communicationClass
        self.valid_commands = config.commands
        self.commandKeys = set(config.commands.keys())
        self.logger  = logging.getLogger("logger.main")

    def process_command(self, command):
        command = command.split(" ")
        if command[0] in self.commandKeys:
            self.logger.debug(f"Running {self.valid_commands[command[0]]}")
            if command[2] != "a":
                self.logger.debug(f"Running on channel {command[2]}")
                if command[1].isnumeric() and command[2].isnumeric():
                    self.communicationClass.send_message(self.valid_commands[command[0]], int(command[2]))
