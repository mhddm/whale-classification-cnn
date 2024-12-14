# Import necessary libraries
import os
import shutil
import pandas as pd
from config import Config


# Ensure necessary directories exist
os.makedirs(Config.ORGANISED_DATA_DIR, exist_ok=True)


# Load labels from excel file
def load_labels(file_path):
    """Load and return the labels from the excel file (in DataFrame data structure)."""
    try:
        labels_df = pd.read_excel(file_path)
        return labels_df
    except Exception as e:
        print(f"Error loading labels file: {e}")
        return None


# Organise audio files by labels
def organise_audio_files(labels_df):
    """Organise audio files into subfolders based on their labels."""
    total_files_copied = 0
    for index, row in labels_df.iterrows():
        # Extract just the filename from the full path in the Excel sheet
        audio_path = row['FileName']                                                # Full path as given in Excel
        filename = os.path.basename(audio_path)                                     # Extract filename only

        # Build the source path dynamically
        labels = row['Labels'].split(',')                                           # Split labels by ',' for multi-labels

        for label in labels:
            # Create a folder for each label
            label_dir = os.path.join(Config.ORGANISED_DATA_DIR, label)              # D:/Australian Database/organised/HW for example
            os.makedirs(label_dir, exist_ok=True)
            target_path = os.path.join(label_dir, filename)                         # D:/Australian Database/organised/HW/57FD5645_90.wav for example

            # Copy the file to the corresponding directory
            try:
                if os.path.exists(audio_path):
                    shutil.copy2(audio_path, target_path)                           # Copy the file
                    total_files_copied += 1
                    print(f"Copied {audio_path} to {target_path}")
                else:
                    print(f"File not found: {audio_path}")
            except Exception as e:
                print(f"Error organizing file {audio_path}: {e}")
                
    print(f"Total files copied: {total_files_copied}")


# Main execution
if __name__ == "__main__":
    labels_df = load_labels(Config.LABELS_FILE)
    if labels_df is not None:
        print("Labels loaded successfully.")
        organise_audio_files(labels_df)
        print("Data extraction completed: Files organized by labels.")
    else:
        print("Failed to load labels.")
