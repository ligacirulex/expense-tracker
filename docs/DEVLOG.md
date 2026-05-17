# Izstrādes žurnāls

## 1. solis: Plānošana
Izveidoju projekta struktūru un aprakstīju moduļus. Sākumā domāju visu likt vienā failā, bet sapratu, ka atdalīšana padara kodu daudz tīrāku. Izdomāju datu struktūru un scenārijus.

## 2. solis: Datu slānis un pamata funkcijas
Uzrakstīju storage.py un pamata app.py izvēlni. Grūtākais bija ievades validācija, īpaši datuma pārbaude ar datetime.strptime(). Pēc pirmās versijas pārbaudīju, ka JSON fails saglabājas pareizi.

## 3. solis: Filtrēšana, kopsavilkums un dzēšana
Pievienoju filtrēšanu pēc mēneša un summas pa kategorijām. Dzēšanas funkcijai pievienoju kļūdu apstrādi, lai programma neuzkārtos. Pārbaudīju ar tukšu sarakstu un nepareiziem ievades numuriem.

## 4. solis: CSV eksports un dokumentācija
Uzrakstīju CSV eksportu ar utf-8-sig, lai Excel pareizi atver latviešu burtus. Sagatavoju README.md un sakārtoju visu projektu. Pārbaudīju, ka eksportētais fails atveras un dati ir pareizi.
