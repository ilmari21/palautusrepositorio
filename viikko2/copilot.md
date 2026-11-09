Koodin täydennysehdotukset tuntuvat usein olevan ihan hyödyllisiä, mutta toisaalta ne tuntuu monesti tekevän myös vääriä johtopäätöksiä siitä, mitä ollaan tekemässä, tuntuu kuin tekoäly olisi "kärsimätön".

Copilotin selitys Pylint-varoituksesta (E401, Unable to import) piti paikkansa.

Agentti teki toimivan ratkaisun sovellusta laajentaessa, tosin agentti jäi pitkäksi aikaa jumiin, ja vasta kun lisäsin kokeilu.py:n kurssimateriaalissa annetulla sisällöllä, sai agentti ratkaisun aikaiseksi nopeammin. Testit toimivat, jouduin tosin kertaalleen pyytämään tekoälyä korjaamaan niitä.

Huomasin, että testien lopussa oli if __name__ == "__main__": unittest.main() -blocki, jota viime viikon testeissä ei ollut. Testien epäonnistuessa aluksi, tekoäly halusi myös alkaa muokkaamaan pyproject.toml -tiedostoa.

Pylint löysi virheen koodista, mutta se ei ollut Copilotin tuotosta; virhe oli kokeilu.py:ssä.

Huomasin, että Copilot käyttö toiminnallisuuksien laajentamisessa vaatii usein, että sen tekemää tuotosta pyydetään parantamaan, osoittamalla sille virhe sen nykyisessä toteutuksessa.
