from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months
from export import export_to_csv
from datetime import date, datetime

CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits"
]

def show_menu():
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def input_date():
    today = date.today().strftime("%Y-%m-%d")
    text = input(f"Datums (YYYY-MM-DD) [{today}]: ").strip()
    if text == "":
        return today
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return text
    except ValueError:
        print("❌ Nederīgs datums.")
        return input_date()

def input_amount():
    text = input("Summa (EUR): ").strip()
    try:
        value = float(text)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print("❌ Ievadi pozitīvu skaitli.")
        return input_amount()

def input_category():
    print("\nKategorija:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"  {i}) {c}")
    choice = input("Izvēlies (1-7): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]
    print("❌ Nederīga izvēle.")
    return input_category()

def add_expense(expenses):
    d = input_date()
    cat = input_category()
    amt = input_amount()
    desc = input("Apraksts: ").strip()

    expense = {
        "date": d,
        "amount": amt,
        "category": cat,
        "description": desc
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\n✓ Pievienots: {d} | {cat} | {amt:.2f} EUR | {desc}")

def show_expenses(expenses):
    if not expenses:
        print("\nNav izdevumu.")
        return

    print("\nDatums       Summa     Kategorija           Apraksts")
    print("-" * 60)
    for e in expenses:
        print(f"{e['date']:<12} {e['amount']:>7.2f}   {e['category']:<18} {e['description']}")
    print("-" * 60)
    print(f"Kopā: {sum_total(expenses):.2f} EUR ({len(expenses)} ieraksti)")

def delete_expense(expenses):
    if not expenses:
        print("\nNav ko dzēst.")
        return

    print("\nIzdevumi:")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}) {e['date']} | {e['amount']:.2f} EUR | {e['category']} | {e['description']}")

    choice = input("\nKuru dzēst? (numurs, 0 lai atceltu): ").strip()
    if choice == "0":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(expenses):
        removed = expenses.pop(int(choice) - 1)
        save_expenses(expenses)
        print(f"✓ Dzēsts: {removed['date']} | {removed['amount']:.2f} EUR | {removed['category']}")
    else:
        print("❌ Nederīgs numurs.")

def filter_month(expenses):
    months = get_available_months(expenses)
    if not months:
        print("\nNav datu.")
        return

    print("\nPieejamie mēneši:")
    for i, m in enumerate(months, start=1):
        print(f"  {i}) {m}")

    choice = input("Izvēlies mēnesi: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(months)):
        print("❌ Nederīga izvēle.")
        return

    year, month = map(int, months[int(choice) - 1].split("-"))
    filtered = filter_by_month(expenses, year, month)
    show_expenses(filtered)

def summary(expenses):
    if not expenses:
        print("\nNav datu.")
        return

    totals = sum_by_category(expenses)
    print("\nKopsavilkums pa kategorijām:")
    print("-" * 40)
    for cat, amt in totals.items():
        print(f"{cat:<20} {amt:>8.2f} EUR")
    print("-" * 40)
    print(f"KOPĀ: {sum_total(expenses):.2f} EUR")

def export_csv(expenses):
    filename = input("Faila nosaukums [izdevumi.csv]: ").strip()
    if filename == "":
        filename = "izdevumi.csv"
    export_to_csv(expenses, filename)
    print(f"✓ Eksportēts: {len(expenses)} ieraksti → {filename}")

def main():
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            filter_month(expenses)
        elif choice == "4":
            summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            export_csv(expenses)
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("❌ Nederīga izvēle.")

if __name__ == "__main__":
    main()
