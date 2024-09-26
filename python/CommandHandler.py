import logging
from statusCache import Status

class CommandHandler:
    def __init__(self, config, storageClass:Status):
        self.logger = logging.getLogger("logger.main")
        self.storageClass = storageClass
        self.valid_commands = config.commands
        self.commandKeys = set(self.config.commands.keys())

    def process_command(self, command):
        command = command.split(" ")
        if command[0] in self.commandKeys:
            if command[2] != "a":
                if command.isnumeric():
                    channels = [int(command[2])]
                else:
                    logging.error(f"Got invalid channel value: {command[2]}")
                    return None
            else:
                channels = self.storageClass.get_tracked_channels()
            for i in channels:
                padded_channel = f"{i:02}"
                self.storageClass.sendMessage(self.commandKeys[command[0]].replace("00", padded_channel), command[1])
                self.logger.debug(f'Ran command {self.commandKeys[command[0]].replace("00", padded_channel)} {command[1]}')
        else:
            if command[0] == "track":
                self.logger.debug(f"started tracking {command[1:]}")
                self.storageClass.track_channel_value(*command[1:])
            elif command[0] == "send":
                self.logger.debug(f"sending command: {command[1:]}")
                self.storageClass.send_command(*command[1:])