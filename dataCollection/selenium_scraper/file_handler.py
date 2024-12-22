import csv

def save_to_csv(data, filename="scraped_content.csv"):
    """
    Save data to a CSV file.
    Data format: List of tuples -> [(url, content), ...]
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Content"])  # Header row
        writer.writerows(data)
    print(f"Data saved to {filename}")

def clean_csv(file_path):
    """
    Remove rows with empty content from the CSV file.
    Returns:
        - List of remaining rows as (URL, Content) pairs.
    """
    valid_rows = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # Retain rows with non-empty content
            if len(row) == 2 and row[1].strip():
                valid_rows.append(row)

    # Overwrite the file with valid rows
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Content"])  # Re-add the header row
        writer.writerows(valid_rows)

    return valid_rows

def load_csv(file_path):
    """
    Load a CSV file and return rows with empty content.
    Returns:
        - List of (URL, Content) pairs
    """
    rows = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # Skip the header row if present
            if row[0] == "URL":
                continue
            # Add rows where content is empty
            if len(row) == 2 and (row[1].strip() == "" or row[1].strip() is None):
                rows.append(row[0])
    return rows

def append_to_csv(file_path, data):
    """
    Append rows to an existing CSV file.
    Args:
        file_path (str): Path to the CSV file.
        data (list): List of (URL, Content) pairs to append.
    """
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)