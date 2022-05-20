import logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#comment this line to show log but there are 5 level of debug
logging.disable(logging.CRITICAL)

logging.debug('strart')
def f(num):
    logging.debug('start is (%s)' %(num))
    total=1
    for i in range (1,num+1):
        total *= i
        logging.debug('And i is %s, total is %s' % (i, total))
    return total
logging.debug('end')

print(f(5))
