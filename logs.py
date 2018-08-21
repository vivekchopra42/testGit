import logging

logger=logging.getLogger(__name__)

#logging.basicConfig(
 #                   format='%(asctime)s %(message)s %Y-%m-%d %H:%M:%S',
  #                  )

console_handler=logging.StreamHandler()

frmtter = logging.Formatter("%(asctime)s ; %(levelname)s ; %(message)s ","%d-%m-%Y: %A-%B : %I : %M : %S : %p ### Local version date & time: %c ")

console_handler.setFormatter(frmtter)

logger.addHandler(console_handler)

logger.setLevel(logging.DEBUG)

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")