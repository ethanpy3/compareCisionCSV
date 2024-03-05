import pandas as pd
import os

# List of your CSV files
csv_files = ['MediaContactCONSUMER.csv', 'MediaContactTRADE.csv', 'MediaContactWAZE.csv']  # Update with your file names

# Dictionary to hold each contact and the files they appear in
contacts = {}

# Iterate through each file
for file in csv_files:
    # Read the current file
    data = pd.read_csv(file)

    # Check each contact in the file
    for index, row in data.iterrows():
        # Construct a unique identifier for each contact
        name_key = f"{row['Contact First Name'].strip().lower()} {row['Contact Last Name'].strip().lower()}"

        # If the contact is already in the dictionary, append the filename to their list
        if name_key in contacts:
            contacts[name_key].add(file)
        else:
            # Otherwise, add the contact to the dictionary
            contacts[name_key] = {file}

# Filter contacts to include only those appearing in multiple files
duplicates = {name: files for name, files in contacts.items() if len(files) > 1}

# Prepare the data for the CSV output
duplicates_list = []
for name, files in duplicates.items():
    first_name, last_name = name.split(' ')
    files_list = '; '.join(files)
    duplicates_list.append([first_name, last_name, files_list])

# Convert the list to a DataFrame
duplicates_df = pd.DataFrame(duplicates_list, columns=['First Name', 'Last Name', 'Files'])

# Save the DataFrame to a new CSV file
duplicates_df.to_csv('duplicates.csv', index=False)
