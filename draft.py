# myapp.py
import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    logger.info('Finished')
    print("finished")

if __name__ == '__main__':
    main()