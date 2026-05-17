# Projekta plāns — Izdevumu izsekotājs (CLI)

## A. Programmas apraksts
Izdevumu izsekotājs ir komandrindas Python lietojums, kas ļauj reģistrēt ikdienas izdevumus, skatīt tos sarakstā, filtrēt pēc mēneša, dzēst ierakstus, redzēt kopsavilkumu pa kategorijām un eksportēt datus CSV failā. Visi dati tiek saglabāti JSON failā starp programmas palaišanām.

## B. Datu struktūra
Viens izdevuma ieraksts tiek glabāts kā vārdnīca:

{
  "date": "2025-02-15",
  "amount": 12.50,
  "category": "Ēdiens",
  "description": "Pusdienas kafejnīcā"
}

Šāda struktūra ir vienkārša, viegli saglabājama JSON formātā un ērti apstrādājama ar Python.

## C. Moduļu plāns

### storage.py
- load_expenses() — nolasa JSON failu
- save_expenses(expenses) — saglabā JSON failu

### logic.py
- sum_total(expenses) — kopējā summa
- filter_by_month(expenses, year, month) — filtrēšana
- sum_by_category(expenses) — summas pa kategorijām
- get_available_months(expenses) — pieejamie mēneši

### export.py
- export_to_csv(expenses, filepath) — CSV eksports

### app.py
- izvēlne, ievades validācija, izsauc funkcijas no citiem moduļiem

## D. Lietotāja scenāriji

1. Lietotājs pievieno izdevumu:
   - ievada datumu, summu, kategoriju, aprakstu
   - programma saglabā un parāda apstiprinājumu

2. Lietotājs filtrē pēc mēneša:
   - izvēlas mēnesi no saraksta
   - programma parāda tikai šī mēneša izdevumus

3. Lietotājs mēģina dzēst neesošu ierakstu:
   - programma parāda kļūdas paziņojumu, neuzkaras

## E. Robežgadījumi

- expenses.json neeksistē → programma izveido tukšu sarakstu
- negatīva summa → kļūdas paziņojums
- nepareizs datuma formāts → kļūdas paziņojums
- tukšs saraksts → “Nav izdevumu”
- dzēšana ar nepareizu numuru → kļūdas paziņojums
