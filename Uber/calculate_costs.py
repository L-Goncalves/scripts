import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv('trips_data-0.csv')

# Convert request_time to datetime
df['request_time'] = pd.to_datetime(df['request_time'])

# Extract year from request_time
df['year'] = df['request_time'].dt.year

# Filter for completed trips only (trips that have a fare)
completed_df = df[df['status'] == 'completed']

# Get all unique currencies
currencies = completed_df['fare_currency'].dropna().unique()

print("=" * 70)
print("UBER COSTS BREAKDOWN BY YEAR AND CURRENCY")
print("=" * 70)

# Calculate costs for each currency
for currency in sorted(currencies):
    currency_df = completed_df[completed_df['fare_currency'] == currency]
    yearly_costs = currency_df.groupby('year')['fare_amount'].sum().sort_index()
    total_cost = currency_df['fare_amount'].sum()

    print(f"\n{currency}:")
    print("-" * 70)

    for year, cost in yearly_costs.items():
        num_trips = len(currency_df[currency_df['year'] == year])
        print(f"  {year}: {cost:,.2f} {currency} ({num_trips} trips)")

    print(f"  {'-' * 66}")
    print(f"  TOTAL: {total_cost:,.2f} {currency} ({len(currency_df)} trips)")

print("\n" + "=" * 70)
print("OVERALL SUMMARY")
print("=" * 70)
print(f"Total completed trips: {len(completed_df)}")
print(f"Total trips (all statuses): {len(df)}")

# Show breakdown by status
print("\nTrips by status:")
status_counts = df['status'].value_counts()
for status, count in status_counts.items():
    print(f"  {status}: {count} trips")

# Show currency distribution
print("\nTrips by currency:")
currency_counts = completed_df['fare_currency'].value_counts()
for currency, count in currency_counts.items():
    total_fare = completed_df[completed_df['fare_currency'] == currency]['fare_amount'].sum()
    print(f"  {currency}: {count} trips (Total: {total_fare:,.2f} {currency})")

print("=" * 70)
