# Uber Trip Cost Calculator

A simple Python script to calculate total Uber costs from trip data, with support for multiple currencies and year-by-year breakdowns.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Export your Uber trip data as CSV from https://myprivacy.uber.com/exploreyourdata/trips (name it `trips_data-0.csv`)
2. Place it in the same directory as the script
3. Run the calculator:

```bash
python3 calculate_costs.py
```

## Expected CSV Format

The script expects a CSV file with the following columns:
- `request_time` - Timestamp of the trip request
- `status` - Trip status (completed, canceled, etc.)
- `fare_amount` - Cost of the trip
- `fare_currency` - Currency of the fare

## Output

The script will display:
- **Year-by-year breakdown** for each currency
- **Total costs** per currency
- **Trip statistics** by status
- **Overall summary** of all trips

## Example Output

```
======================================================================
UBER COSTS BREAKDOWN BY YEAR AND CURRENCY
======================================================================

Brazilian Real:
----------------------------------------------------------------------
  2023: 4,476.05 Brazilian Real (201 trips)
  2024: 3,385.36 Brazilian Real (133 trips)
  2025: 4,886.35 Brazilian Real (200 trips)
  ------------------------------------------------------------------
  TOTAL: 14,833.35 Brazilian Real (614 trips)
======================================================================
```
