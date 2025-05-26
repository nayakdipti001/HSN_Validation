import pandas as pd

# Load the Excel file
file_path = "HSN_Master_Data.xlsx"
df = pd.read_excel(file_path)

# Clean column names and make sure HSN codes are strings
df.columns = df.columns.str.strip()
df['HSNCode'] = df['HSNCode'].astype(str)

# Ask for multiple HSN codes
user_input = input("Enter HSN code(s), separated by commas: ").strip()

# Split input into a list and remove spaces
codes = [code.strip() for code in user_input.split(",")]

print("\n🔍 Validation Results:")
for code in codes:
    if not code.isdigit():
        print(f"❌ {code}: Invalid format (must be numeric)")
    elif code in df['HSNCode'].values:
        desc = df[df['HSNCode'] == code]['Description'].values[0]
        print(f"✅ {code}: VALID – {desc}")
    else:
        print(f"❌ {code}: Not found in HSN master data")
