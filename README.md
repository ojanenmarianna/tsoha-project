# Tsoha - treenipäiväkirja 


Sovellus listaa kaikkien käyttäjien tallentamat treenit sekä käyttäjän itse tallentamat treenit. Käyttäjä näkee omat ja toisten tallentamat treenit ja voi lisätä kommentteja niihin. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä. Sovellus laskee sivun vierailijat ja tallennettujen treenien määrän, niin kaikilta käyttäjiltä, kuin myös jokaisen käyttäjän omien treenien määrän.

Sovelluksen testausta varten on luotu kaksi testikäyttäjää:
- Peruskäyttäjä: test, salasana: testPassword1
- Ylläpitäjä: testadmin, salasana testPassword2

## Toteutetut ominaisuudet:

- Käyttäjä pystyy kirjautumaan sisään ja ulos, sekä luomaan uuden tunnuksen
- Käyttäjä pystyy luomaan ja tallentamaan uuden treenin
- Käyttäjä voi kommentoida omiaan ja muiden tallentamia treenejä
- Käyttäjä pystyy poistamaan tallentamansa treenin
- Ylläpitäjä pystyy poistamaan kenen tahansa treenin sekä kenet vaan käyttäjän

## Tulossa olevat ominaisuudet:
 
- Peruskäyttäjä pystyy muokkaamaan treenin sisältöä myöhemmin 
- Käyttäjä voi etsiä treenin nimen kategorian perusteella (juoksu, voimannosto, ym.) 
- Ylläpitäjä pystyy poistamaan kenen vaan kommentin

Sovellus on testattavissa [Herokussa](https://tsoha-project.herokuapp.com).
