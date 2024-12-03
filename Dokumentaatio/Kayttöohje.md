Käynnistäminen.

Mene ja tee .env tiedosto, jossa on: 
DATABASE_URL= (omat tiedot)
TEST_ENV=true
SECRET_KEY=

Jos sovellus iktee tietokantaan liittyvästä ongelmasta:
kirjoita terminaaliin:
python src/db_helper.py tai python src/init_database.py
ja sitten kokeile uudestaan käynnistää index.py

varmista myös että tarvittavat dependencies ladataan
