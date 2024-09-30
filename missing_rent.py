import pandas as pd
import json

def find_missing_rent_payments(file_path):
    # Step 1: Load the rent transaction data from a CSV file
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return json.dumps({"error": f"Failed to read the file: {str(e)}"}, indent=4)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Determine start and end dates based on the data
    start_date = df['Date'].min().strftime('%Y-%m-%d')
    end_date = df['Date'].max().strftime('%Y-%m-%d')

    # Step 2: Extract the month from the date and group by PropertyId and Month
    df['Month'] = df['Date'].dt.to_period('M')
    grouped = df.groupby(['PropertyId', 'Month']).size().reset_index(name='Count')

    # Step 3: Create a dynamic range of months based on the start and end dates
    months_range = pd.date_range(start=start_date, end=end_date, freq='M').to_period('M')

    results = []
    for property_id in df['PropertyId'].unique():
        # Get the months for this specific property
        received_months = grouped[grouped['PropertyId'] == property_id]['Month']

        # Identify the missing months for the property
        missing_months = months_range[~months_range.isin(received_months)]

        # Step 4: Collect results for missing months
        for missing_month in missing_months:
            results.append({
                "propertyId": property_id,
                "month": str(missing_month)
            })

    # Convert the results list to JSON format
    return json.dumps(results, indent=4)

# Example usage
if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Please enter the path to the rent transaction CSV file: ")

    missing_payments_json = find_missing_rent_payments(file_path)
    print(missing_payments_json)
