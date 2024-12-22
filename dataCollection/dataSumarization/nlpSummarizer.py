import pandas as pd

# Load the input CSV file
input_file = "dataCollection/data/nlps/nlps_useCase_scenrios.csv"  
output_file = "dataCollection/data/nlps/summarized_nlps.csv"

# Read the input CSV file
df = pd.read_csv(input_file)

# Create a new dataframe for the output
output_data = {
    "url": [],
    "summarizedText": []
}

# Process each row and generate the summarized text
for index, row in df.iterrows():
    nlp_template = row.get("NLP", "")
    example = str(row.get("Example", "")).replace("In this example", "")
    use_case = row.get("Data", "") 
    scenarios = row.get("Detailed Use Case Scenarios", "")
    
    # Format the summarized text
    summarized_text = (
        f"**NLP Template:** {nlp_template}\n"
        f"**Example Use Case:** {example}\n"
        f"**Detailed Scenarios:** {scenarios}"
    )
    
    # Append to the output data
    output_data["url"].append("")
    output_data["summarizedText"].append(summarized_text)

# Create the output dataframe
output_df = pd.DataFrame(output_data)

# Save to the new CSV file
output_df.to_csv(output_file, index=False)

print(f"New CSV file created: {output_file}")
