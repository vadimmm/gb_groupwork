import logging

logging.basicConfig(filename='logging.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s: %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')