import os

from commands.command import Command

GITHUB_MODULE = 'githubmodul.py'
REPO_MODULE = 'distrorepo.py'


def call(self, command):
    module = GITHUB_MODULE if command == Command.GIT else REPO_MODULE
    os.system(f"python3 {self.prefix}/share/felis/{module}")
