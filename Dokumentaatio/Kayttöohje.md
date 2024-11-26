Käynnistäminen.

Mene ja tee .env tiedosto, jossa on: 
DATABASE_URL= (omat tiedot)
TEST_ENV=true
SECRET_KEY=

Jos sovellus iktee todo tableen liittyvästä ongelmasta:
kirjoita terminaaliin:
python src/db_helper.py
ja sitten kokeile uudestaan käynnistää index.py