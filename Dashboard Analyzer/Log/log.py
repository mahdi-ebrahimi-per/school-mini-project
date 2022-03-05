import logging


class log:
    def __init__(self, filename='app.log'):
        
        logging.basicConfig(filename=filename, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s : %(message)s - %(process)d')

        self.filename = filename


    def log (self, levelname, massage):
        try :
            if levelname == 'error':
                logging.error(massage) #exc_info=True

            if levelname == 'warning':
                logging.warning(massage)

            if levelname == 'debug':
                logging.debug(massage)

            if levelname == 'info':
                logging.info(massage)

            if levelname == 'critical':
                logging.critical(massage)

            if levelname == 'exception':
                logging.exception(massage) 

        except:
            raise ValueError("levelname is wrong (it must be string)")

    def clear_log(self):
        open(self.filename, 'w').close()



log = log()

# log.log('error', 'h')

try :
    kj + i

except:
    log.log('exception', "error exception")