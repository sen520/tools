import datetime
import logging


def create_logger(name):
    """
    create log file

    :param name: file of absolute path
    :return: log object
    """
    log = logging.getLogger(name)
    log.handlers = []
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.FileHandler(name))
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    log.addHandler(stream_handler)
    return log


def create_log_decorator(filename='log'):
    def logger(func):
        def write_file(*args, **kwargs):
            log = create_logger(filename + '.log')
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log.debug('\nstart time: ' + start_time)
            log.debug('func: ' + func.__name__ + '\nargs: ' + str(args) + '\nkwargs:' + str(kwargs))
            try:
                func(*args, **kwargs)
            except Exception as e:
                log.error(e)
                raise e
            end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log.debug('end time: ' + end_time)

        return write_file

    return logger