import pandas as pd

# Convert a structured JSON file to a CSV file.
def json_to_csv(json_file, csv_file):
    
    #:param json_file: Path to the input JSON file. 
    #:param csv_file: Path to the output CSV file. --> empty
    
    try:
        df = pd.read_json(json_file)
        df.to_csv(csv_file, encoding='utf-8', index=False)
        print(f"Successfully converted {json_file} to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
#json_to_csv("someFile.json", "someFile.csv")  # Replace with actual file names
