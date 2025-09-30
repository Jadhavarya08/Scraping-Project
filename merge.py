# merge_excel_files.py
import pandas as pd
import glob

# List of all your files
files = [
    "Kansas_Tax_store_scraped_data.xlsx",
    "Output_Kansas_Coaching Institutes_scraped_data.xlsx",
    "Kansas_Beauty&PersonalCare.xlsx",
    "Output_Kansas_Consultant_scraped_data.xlsx",
    "Output_Kansas_Cafe_scraped_data.xlsx",
    "Kansas_Catering_store_scraped_data.xlsx",
    "Kansas_Furniture_store_scraped_data.xlsx",
    "Output_Kansas_Hospital & Clinics_scraped_data.xlsx",
    "Output_Kansas_Real Estate Agency_scraped_data.xlsx",
    "Output_Kansas_Beauty&PersonalCare_scraped_data.xlsx",
    "Kansas_Restaurants_store_scraped_data.xlsx",
    "Output_Kansas_Legal Services_scraped_data.xlsx",
    "Kansas_Fitness_store_scraped_data.xlsx",
    "Output_Kansas_Financial Planner_scraped_data.xlsx",
    "Kansas_clothing_store_scraped_data.xlsx",
    "Kansas_jwellery_store_scraped_data.xlsx"
]

# Final merged dataframe
all_data = []

# Load each file
for f in files:
    try:
        df = pd.read_excel(f)

        # Standardize column names (strip spaces and lower them for consistency)
        df.columns = df.columns.str.strip()

        # Ensure only the required columns exist
        required_cols = ["Business Name", "Email", "Phone", "Website", "Address", "Source URL", "Category"]
        for col in required_cols:
            if col not in df.columns:
                df[col] = ""  # Add missing column as empty

        df = df[required_cols]  # Keep only required columns
        all_data.append(df)

        print(f"✅ Loaded {f} with {len(df)} rows")
    except Exception as e:
        print(f"❌ Failed to load {f}: {e}")

# Concatenate all data
merged_df = pd.concat(all_data, ignore_index=True)

# Drop duplicates by Business Name only
merged_df = merged_df.drop_duplicates(subset=["Business Name"], keep="first")

# Save to final Excel
output_file = "Kansas_All_Businesses_Merged.xlsx"
merged_df.to_excel(output_file, index=False)
    
print(f"🎉 Merge complete! Final file saved as {output_file} with {len(merged_df)} unique businesses.")
