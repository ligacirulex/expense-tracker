from datetime import datetime

def sum_total(expenses):
    """Aprēķina kopējo summu."""
    return round(sum(e["amount"] for e in expenses), 2)

def filter_by_month(expenses, year, month):
    """Atgriež izdevumus konkrētam mēnesim."""
    result = []
    for e in expenses:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            result.append(e)
    return result

def sum_by_category(expenses):
    """Atgriež summas pa kategorijām."""
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return {k: round(v, 2) for k, v in totals.items()}

def get_available_months(expenses):
    """Atgriež sarakstu ar pieejamajiem YYYY-MM mēnešiem."""
    months = set()
    for e in expenses:
        months.add(e["date"][:7])
    return sorted(months)
