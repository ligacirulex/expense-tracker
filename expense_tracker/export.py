import csv

def export_to_csv(expenses, filepath):
    """Eksportē izdevumus CSV failā."""
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
        for e in expenses:
            writer.writerow([
                e["date"],
                f"{e['amount']:.2f}",
                e["category"],
                e["description"]
            ])
