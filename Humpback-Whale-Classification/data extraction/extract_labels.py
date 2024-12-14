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

if not os.path.isdir(Config.RAW_DATA_DIR):
    logging.error(f"Raw data directory not found: {Config.RAW_DATA_DIR}")
    exit(1)
    
if not os.path.isfile(Config.LABELS_FILE):
    logging.error(f"Labels file not found: {Config.LABELS_FILE}")
    exit(1)


# Load labels from excel file
def load_labels(file_path):
    """
    Load and return the labels from the excel file.
    
    Args: 
        file_path (str): Path to the excel file containing filename and labels.
        
    Returns: 
        pd.DataFrame: DataFrame containing the labels if loaded successfully; otherwise, None.
    """
    try:
        labels_df = pd.read_excel(file_path)
        logging.info("Labels file loaded successfully.")
        return labels_df
    
    except Exception as e:
        logging.error(f"Error loading labels file: {e}")
        return None


# Organise audio files by labels
def organise_audio_files(labels_df):
    """
    Organise audio files into subfolders based on their labels. 
    In my excel sheet, some files may have more than 1 label. Files with multiple labels will be copied into each respective folder.
    
    Args: 
        labels_df: DataFrame containing file paths and labels.
    
    Returns:
        int: Total number of files successfully copied.
        None: If the DataFrame is missing required columns ('Labels' or 'FileName').
    """
    
    if 'Labels' not in labels_df.columns or 'FileName' not in labels_df.columns:        # Data integrity check
        logging.error("Missing required columns in labels file.")
        return None
    
    total_files_read = 0
    total_files_copied = 0
    
    for index, row in labels_df.iterrows():
        # Extract just the filename from the full path in the Excel sheet
        total_files_read += 1
        audio_path = row['FileName']                                                # Full path as given in Excel
        filename = os.path.basename(audio_path)                                     # Extract filename only

        # Build the source path dynamically
        labels = [label.strip() for label in row['Labels'].split(',')]              # Removes trailing/leading whitespaces and split labels by ',' for multi-labels. Returns a list

        for label in labels:
            # Create a folder for each label
            label_dir = os.path.join(Config.ORGANISED_DATA_DIR, label)              # D:/Australian Database/organised/HW for example
            os.makedirs(label_dir, exist_ok=True)
            target_path = os.path.join(label_dir, filename)                         # D:/Australian Database/organised/HW/57FD5645_90.wav for example

            # Copy the file to the corresponding directory
            try:
                source_exists = os.path.exists(audio_path)
                target_exists = os.path.exists(target_path)
                
                if source_exists and not target_exists:                             # Avoid redudant copying                            
                    shutil.copy2(audio_path, target_path)                           # Copy the file
                    total_files_copied += 1
                    logging.info(f"Copied {audio_path} to {target_path}")
                else: 
                    if not source_exists:
                        logging.warning(f"Row {index}: Source file not found: {audio_path}")
                    else:   
                        logging.info(f"Row {index}: File already exists: {target_path}")
                    
            except Exception as e:
                logging.error(f"Error organising file {audio_path}: {e}")
    
    logging.info(f"Total files read: {total_files_read}")
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
        