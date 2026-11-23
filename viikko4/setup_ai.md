Mielestäni agentti poisti toisteisuuden hyvin, mock-oliot luodaan setUpissa eikä niitä näin ollen tarvitse luoda erikseen jokaisessa testissä. En tiedä onko testikoodi varsinaisesti helpompi lukea, mutta selvästi lyhyempi ainakin.

Agentti ei muuttanut itse testien toiminnallisuutta; tarkistus tapahtuu edelleen assert_once_called_with:llä.

En korjannut agentin tekemiä muutoksia.
