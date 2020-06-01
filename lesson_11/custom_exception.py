import time
import logging

logging.basicConfig(filename='log.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s % (message)s')

logger=logging.getLogger(__name__)

class NumberNotInRangeError(Exception):
    def __init__(self, number):
        self.message = "Number {} is not in range (5, 10)".format(number)
        super().__init__(self.message)

log_file = open('log.txt', 'a')
number = int(input("Enter number from 5 to 10: "))
try:
    if not 5 <= number <= 10:
        raise NumberNotInRangeError(number)

except NumberNotInRangeError as err:
    logger.debug(err)



    
