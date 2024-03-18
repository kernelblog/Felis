import os
import sys

from commands import media, remove, repo, clone
from commands.command import Command
from utils import Utils
from validator import Validator


class Felis:
    def __init__(self):
        self.prefix = os.getenv("PREFIX", "/usr" if len(os.getenv("PREFIX", "")) <= 2 else "")
        self.sudo = "" if self.prefix != "/usr" else "sudo "

    def process_command(self, args):
        no_command = len(args) < 2
        if no_command or args[1] == Command.HELP.value:
            Utils.print_help_message()
            return

        try:
            command = Command(args[1])
        except ValueError:
            Utils.print_help_message()
            return

        if command == Command.CHECK_UPDATES:
            Validator.check_for_updates(self)
        elif command == Command.REMOVE:
            remove.call(self=self)
        elif command in [Command.MUSIC, Command.VIDEO]:
            media.call(self=self, args=args)
        elif command in [Command.GIT, Command.REPO]:
            repo.call(self=self, command=command)
        elif command == Command.CLONE:
            clone.call(args=args)
        else:
            Utils.print_help_message()


def main():
    felis = Felis()
    felis.process_command(sys.argv)


if __name__ == "__main__":
    main()
