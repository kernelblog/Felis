from enum import Enum


class Command(Enum):
    HELP = '-y'
    CHECK_UPDATES = '-g'
    REMOVE = '-s'
    MUSIC = '-mp3'
    VIDEO = '-mp4'
    GIT = "-git"
    REPO = "-repo"
    CLONE = '-clone'
