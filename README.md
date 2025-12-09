[![CI badge](https://github.com/alexisvarjo/ohtu-miniprojekti/actions/workflows/ci.yaml/badge.svg)](https://github.com/alexisvarjo/ohtu-miniprojekti/actions/workflows/ci.yaml) [![Lint (pylint)](https://github.com/alexisvarjo/ohtu-miniprojekti/actions/workflows/lint.yaml/badge.svg?branch=master)](https://github.com/alexisvarjo/ohtu-miniprojekti/actions/workflows/lint.yaml) [![codecov](https://codecov.io/gh/alexisvarjo/ohtu-miniprojekti/graph/badge.svg?token=WLCS6X4USN)](https://codecov.io/gh/alexisvarjo/ohtu-miniprojekti)

## Viitteiden hallinta järjestelmä

Ryhmä: Kvokaalit, ohtu miniprojekti syksy 2025 TKT20006

Sovellus on verkkosivu, mikä mahdollistaa helpon viitteiden hallinnan.

### Toiminnot

- Article, Book ja Inproceeding-viitetyyppien lisääminen
    - Manuaalinen
    - ACM Digital Library linkki
    - DOI tunniste
- Viitteiden yhteydessä PDF:n lisäys
- Viitteiden muokkaus ja poisto
- Viitteiden listaus etusivulla
- Viitteiden filteröinti
    - Viitetyyppi
    - Tekijä, otsikko ja tägi
    - Vuosi
- Viitteiden lataaminen
    - BibTex selaimessa
    - BibTex tiedosto

Product backlog ja sprint backlog: https://docs.google.com/spreadsheets/d/1tK9AVzTZSkeHgW1EZFT_ms2w0wZbGu9LWFU_PPOqzLw/edit?gid=1#gid=1

### Asennusohjeet (Linux):
- Ennen käyttöä täytyy [Python](https://www.python.org/) ja [poetry](https://python-poetry.org/) olla ladattuina. Projekti vaatii myös [PostgreSQL](https://www.postgresql.org/)-tietokannan toimiakseen
- Lataa projekti tältä Github sivulta
- Luo projektin kansion juureen tiedosto .env ja määrittele siihen seuraavat muuttujat
    - `DATABASE_URL=`: täydennä PostgreSQL tietokannan polku
    - `TEST_ENV=`: täydennä false tai true (testiympäristö)
    - `SECRET_KEY=`: täydennä tietokantasi salainen avain
- Lataa tarvittavat riippuvuudet: `poetry install`
- Käynnistä virtuaaliympäristö: `eval $(poetry env activate)`
- Luo tietokantataulutu (vain ennen ensimmäistä käynnistystä): `python src/db_helper.py`
- Käynnistä ohjelma: `python3 src/index.py`
- Ohjelma käynnistyy osoiteeseen `http://127.0.0.1:5001`

### Käyttöohje:
Sovelluksen etusivulla näkyvät kaikki lisätyt viitteet uusimmasta vanhimpaan. Add New valikon kautta. Etusivulla voi filteröidä lähteitä ja tulostaa BibTex tiedosto.

### Definition of done:
- User storyilla hyväksymiskriteerit
    - Automaattinen robot-testaus (jos mahdollista)
- Kohtuullinen testikattavuus
- Asiakas pääsee näkemään koko ajan koodin ja testien tilanteen CI-palvelusta
- Koodin ylläpidettävyyden tulee olla mahdollisimman hyvä
    - Järkevä nimeäminen
    - Järkevä/selkeä ja perusteltu arkkitehtuuri
    - Yhtenäinen koodityyli (valvotaan Pylintin avulla)
