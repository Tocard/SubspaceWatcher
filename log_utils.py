import logging
import colorlog

global Logger


class LoggerUtils:
    DEBUG = 1
    INFO = 2
    SUCCESS = 3
    WARNING = 4
    FAILED = 5

    def __init__(self, debug: bool):
        logging.addLevelName(self.DEBUG, 'DEBUG')
        logging.addLevelName(self.INFO, 'INFO')
        logging.addLevelName(self.SUCCESS, 'SUCCESS')
        logging.addLevelName(self.WARNING, 'WARNING')
        logging.addLevelName(self.FAILED, 'FAILED')
        color_mapping = {
            'DEBUG': 'yellow',
            'DEFAULT': 'grey',
            'INFO': 'cyan',
            'SUCCESS': 'green',
            'WARNING': 'purple',
            'FAILED': 'red'
        }
        if debug:
            log_pattern = '%(asctime)s %(log_color)s%(levelname)s%(reset)s [%(filename)s:%(lineno)s - %(funcName)20s() ] | %(name)s | %(log_color)s%(message)s'
            level = self.DEBUG
        else:
            log_pattern = '%(asctime)s %(log_color)s%(levelname)s%(reset)s | %(name)s | %(log_color)s%(message)s'
            level = self.INFO

        self.formatter = colorlog.ColoredFormatter(log_pattern, log_colors=color_mapping)

        self.subspace_watcher = logging.getLogger('subspace.watcher')
        self.subspace_watcher_handler = logging.StreamHandler()
        self.subspace_watcher_handler.setFormatter(self.formatter)
        self.subspace_watcher.addHandler(self.subspace_watcher_handler)
        self.subspace_watcher.setLevel(level)

    def success(self, name):
        self.subspace_watcher.log(self.SUCCESS, "{}".format(name))

    def warning(self, name):
        self.subspace_watcher.log(self.WARNING, "{}".format(name))

    def info(self, name):
        self.subspace_watcher.log(self.INFO, "{}".format(name))

    def failed(self, name):
        self.subspace_watcher.log(self.FAILED, "{}".format(name))


def init_logger(debug: bool):
    global Logger
    Logger = LoggerUtils(debug)
