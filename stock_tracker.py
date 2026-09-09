"""
CodeAlpha Internship — Task 2: Stock Portfolio Tracker
Author: Aaron Baidoo (RoniKid)
Description: User inputs stock symbols and quantities. The tracker looks
             up prices from a hardcoded dictionary, calculates total
             investment value, and optionally saves a CSV report.
"""

import csv
import os
from datetime import datetime

# ── Hardcoded stock prices (USD) ───────────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  189.50,   # Apple
    "TSLA":  248.00,   # Tesla
    "GOOGL": 175.20,   # Alphabet
    "AMZN":  185.60,   # Amazon
    "MSFT":  415.30,   # Microsoft
    "META":  490.80,   # Meta
    "NVDA":  875.40,   # NVIDIA
    "NFLX":  620.10,   # Netflix
}


def show_available_stocks():
    """Print the list of supported tickers and their current prices."""
    print("\n  Available stocks:")
    print(f"  {'Ticker':<8} {'Price (USD)':>12}")
    print("  " + "-" * 22)
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<8} ${price:>11.2f}")
    print()


def get_portfolio_input():
    """Interactively collect the user's stock holdings."""
    portfolio = {}   # {ticker: quantity}

    print("\n  Enter your stocks. Type 'done' when finished.")
    print("  (Type 'list' to see available tickers)\n")

    while True:
        ticker = input("  Stock symbol: ").strip().upper()

        if ticker == "DONE":
            break
        if ticker == "LIST":
            show_available_stocks()
            continue
        if ticker not in STOCK_PRICES:
            print(f"  ✗  '{ticker}' not found. Type 'list' to see supported tickers.\n")
            continue

        # Quantity input with validation
        while True:
            qty_str = input(f"  Quantity of {ticker}: ").strip()
            try:
                quantity = float(qty_str)
                if quantity <= 0:
                    print("  ✗  Quantity must be greater than 0.")
                else:
                    break
            except ValueError:
                print("  ✗  Please enter a valid number.")

        # If the ticker was already entered, add to existing quantity
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        print(f"  ✓  Added {quantity} share(s) of {ticker}.\n")

    return portfolio


def calculate_portfolio(portfolio):
    """Return a list of row dicts and the grand total."""
    rows = []
    total = 0.0

    for ticker, quantity in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * quantity
        total += value
        rows.append({
            "Ticker":   ticker,
            "Quantity": quantity,
            "Price":    price,
            "Value":    value,
        })

    return rows, total


def display_report(rows, total):
    """Print a formatted portfolio summary to the console."""
    print("\n" + "=" * 50)
    print("        PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>12} {'Value':>14}")
    print("  " + "-" * 44)

    for row in rows:
        print(
            f"  {row['Ticker']:<8}"
            f" {row['Quantity']:>6.2f}"
            f"  ${row['Price']:>10.2f}"
            f"  ${row['Value']:>12.2f}"
        )

    print("  " + "-" * 44)
    print(f"  {'TOTAL':>28}  ${total:>12.2f}")
    print("=" * 50)


def save_to_csv(rows, total):
    """Save the portfolio report to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.csv"

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Ticker", "Quantity", "Price (USD)", "Value (USD)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow({
                "Ticker":       row["Ticker"],
                "Quantity":     row["Quantity"],
                "Price (USD)":  row["Price"],
                "Value (USD)":  row["Value"],
            })

        # Append a total row
        writer.writerow({
            "Ticker":       "TOTAL",
            "Quantity":     "",
            "Price (USD)":  "",
            "Value (USD)":  round(total, 2),
        })

    print(f"\n  ✓  Report saved to '{filename}'")
    return filename


def main():
    print("\n" + "=" * 50)
    print("      CodeAlpha — Stock Portfolio Tracker")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio_input()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    rows, total = calculate_portfolio(portfolio)
    display_report(rows, total)

    save_choice = input("\n  Save report to CSV? (y/n): ").strip().lower()
    if save_choice == "y":
        save_to_csv(rows, total)

    print("\n  Goodbye!\n")


if __name__ == "__main__":
    main()
