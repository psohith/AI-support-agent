import csv
from langchain.text_splitter import MarkdownTextSplitter

# Function to split markdown content using MarkdownTextSplitter
def split_text_with_langchain(text, chunk_size, chunk_overlap):
    splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(text)
    return chunks

# Main function to process the CSV
def process_csv(input_csv, output_csv, chunk_size=1500, chunk_overlap=200):
    rows_to_write = []

    with open(input_csv, "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            url = row["url"]
            summarized_text = row["summarizedText"]

            # Split the summarizedText into chunks using MarkdownTextSplitter
            chunks = split_text_with_langchain(summarized_text, chunk_size, chunk_overlap)

            # Add each chunk as a separate row
            for chunk in chunks:
                rows_to_write.append({"url": url, "summarizedText": chunk})

    # Write the updated data to a new CSV file
    with open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["url", "summarizedText"])
        writer.writeheader()
        writer.writerows(rows_to_write)

    print(f"Updated CSV written to {output_csv}")

# Example usage
process_csv("dataCollection/data/guides/summarized_content.csv", "dataCollection/data/guides/chunked_summarized_content.csv")
