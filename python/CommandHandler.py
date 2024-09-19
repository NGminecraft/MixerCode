class CommandHandler:
    def __init__(self, config, communicationClass):
        self.communicationClass = communicationClass
        self.valid_commands = config.commands
        self.commandKeys = set(self.config.commands.keys())

    def process_command(self, command):
        command = command.split(" ")
        if command[0] in self.commandKeys:
            if command[2] != "a":
                if type(command[1]).isnumeric and type(command[2]).isnumeric():
                    communicationClass.sendMessage(*command[0:3])
