import logging
import sys
import sqlite3

logging.basicConfig(
    filename='teht4.log',
    level=logging.DEBUG)
logger = logging.getLogger()

con = sqlite3.connect("teht4.db")
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS '
                           'logs (lvl TEXT, msg TEXT);''')

def kayttisoikeus(uusi):
    logger.warning("Uusi kaytto-oikeus: %s" % repr(uusi))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ei näin :(")
        exit(1)

    con.execute('INSERT INTO logs VALUES ("INFO","%s")' % sys.argv[1])

    print("Lisättiin lokitiedostoon!")
    con.commit()
    con.close()