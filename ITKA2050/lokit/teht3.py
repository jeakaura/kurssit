import logging
import sys

logging.basicConfig(
    filename='teht3.log',
    level=logging.DEBUG)
logger = logging.getLogger()

def kayttisoikeus(uusi):
    logger.warning("Uusi kaytto-oikeus: %s" % repr(uusi))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ei näin :(")
        exit(1)
    logger.info(repr(sys.argv[1]))
    print("Lisättiin lokitiedostoon!")