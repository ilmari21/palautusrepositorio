# Projektiohjeet

## Arkkitehtuuri

- Flask-sovellus käynnistyy tiedostosta `src/app.py`. Reitit renderöivät Jinja-pohjat hakemistosta `src/templates/` ja tekevät uudelleenohjaukset kirjautumisen tai rekisteröitymisen jälkeen.
- Kirjautumisen ja rekisteröitymisen säännöt kuuluvat tiedoston `src/services/user_service.py` `UserService`-luokkaan. Reitittimien tulee pysyä ohuina: ne lukevat lomaketiedot, kutsuvat palvelua ja käsittelevät uudelleenohjaukset sekä flash-virheet.
- `src/repositories/user_repository.py` on muistiin perustuva repository. Sovelluksen jakama moduulitason `user_repository`-instanssi säilyttää tilan, joten `/tests/reset`-reitti tyhjentää sen hyväksymistestien välissä.
- Selaimen hyväksymistestit ovat hakemistossa `src/tests/` ja käyttävät Robot Framework Browseria. Jaettu selaimen alustus, URL-osoitteet ja sivutarkistukset kuuluvat tiedostoon `src/tests/resource.robot`; testisarjakohtaiset työnkulut kuuluvat vastaavaan `.robot`-tiedostoon.
- `src/AppLibrary.py` on Robot Framework -kirjasto testien HTTP-alustusta, kuten sovelluksen nollaamista ja käyttäjän luomista, varten. Se käyttää osoitetta `http://localhost:5001`.

## Koonti ja testaus

- Projekti käyttää uv:ta. Riippuvuudet synkronoidaan komennolla `uv sync`, ja projektin komennot suoritetaan muodossa `uv run ...`.
- Käynnistä sovellus virtuaaliympäristössä komennolla `python3 src/index.py`. Sovellus toimii portissa `5001`.
- Sovelluksen on oltava käynnissä portissa `5001` Robot Framework -testien aikana.
- Aja kaikki Robot Framework -testit komennolla `uv run robot src/tests`.
- Yksittäisen testisarjan voi ajaa komennolla `uv run robot src/tests/register.robot` tai `uv run robot src/tests/login.robot`.
- Yksittäisen testin voi ajaa komennolla `uv run robot -t "Register With Valid Username And Password" src/tests`.
- Projektille ei ole määritetty erillistä build- tai lint-komentoa.

## Konventiot

- Selaintestit olettavat sovelluksen kuuntelevan portissa `5001`; jos porttia muutetaan, päivitä sekä `${SERVER}` tiedostossa `src/tests/resource.robot` että perusosoite tiedostossa `src/AppLibrary.py`.
- Testien alustuksen tulee nollata sovelluksen tila ennen jokaista testiä. Nykyiset rekisteröitymistestit luovat `kalle`-testikäyttäjän ja siirtyvät sen jälkeen osoitteeseen `${REGISTER_URL}`.
- Rekisteröitymislomake lähettää kentät `username`, `password` ja `password_confirmation`; käytä tiedostossa `src/templates/register.html` määriteltyjä tarkkoja elementtien id-arvoja.
- Browser-kirjaston `Fill Secret` vastaanottaa Robotin skalaarimuuttujat muodossa `$password`, ei muodossa `${password}`.
- Käyttäjätunnuksen ja salasanan validointi tapahtuu `src/services/user_service.py`-tiedoston `UserService`-luokan `validate`-metodissa. Metodi tarkistaa myös salasanan vahvistuksen ja käyttäjätunnuksen ainutkertaisuuden.
- Validointi nostaa `UserInputError`-poikkeuksen puuttuvista kentistä, liian lyhyistä käyttäjätunnuksista tai salasanoista, eroavista salasanoista ja päällekkäisistä käyttäjätunnuksista. Säilytä nämä palvelutason tarkistukset äläkä toista niitä reitittimissä.
