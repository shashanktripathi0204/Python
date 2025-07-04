import logging

#  configure Logging
print("=== INSIDE logger.py ===")

logging.basicConfig(
    # setting the level to DEBUG will capture all levels of logs
    # including DEBUG, INFO, WARNING, ERROR, and CRITICAL
    # setting level to WARNINGS will only capture WARNING, ERROR, and CRITICAL
    # setting level to ERROR will only capture ERROR and CRITICAL
    # setting level to CRITICAL will only capture CRITICAL
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename= 'logfile.log',
    filemode = 'w', # 'w' for write mode, 'a' for append mode,
    force=True  # Force the configuration to be applied even if logging is already configured
)

print("Logging is configured. You can now use the logging module in your scripts.")