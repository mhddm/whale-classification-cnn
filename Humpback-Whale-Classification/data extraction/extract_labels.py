# Import necessary libraries
import os
import shutil
import pandas as pd
from config import Config
import logging


# Configure logging
logging.basicConfig(level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure necessary directories exist
os.makedirs(Config.ORGANISED_DATA_DIR, exist_ok=True)


# Load labels from excel file
def load_labels(file_path):
    """Load and return the labels from the excel file (in DataFrame data structure)."""
    try:
        labels_df = pd.read_excel(file_path)
        logging.info("Labels file loaded successfully.")
        return labels_df
    except Exception as e:
        logging.error(f"Error loading labels file: {e}")
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
                    if not os.path.exists(target_path):                             # Avoid redudant copying
                        shutil.copy2(audio_path, target_path)                       # Copy the file
                        total_files_copied += 1
                        logging.info(f"Copied {audio_path} to {target_path}")
                    else: 
                        logging.info(f"File already exists: {target_path}")
                else:
                    logging.warning(f"Source file not found: {audio_path}")
            except Exception as e:
                logging.error(f"Error organising file {audio_path}: {e}")
                
    logging.info(f"Total files copied: {total_files_copied}")
    return total_files_copied


# Main execution
if __name__ == "__main__":
    labels_df = load_labels(Config.LABELS_FILE)
    if labels_df is not None:
        logging.info("Labels loaded successfully.")
        total_files_copied = organise_audio_files(labels_df)
        logging.info(f"Data extraction completed: {total_files_copied} files organised by labels.")
    else:
        logging.error("Failed to load labels.")
