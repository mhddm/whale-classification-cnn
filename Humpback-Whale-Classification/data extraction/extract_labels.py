# Import necessary libraries
import os
import shutil
import pandas as pd
from config import Config


# Ensure necessary directories exist
os.makedirs(Config.ORGANISED_DATA_DIR, exist_ok=True)


# Load labels from excel file
def load_labels(file_path):
    """Load and return the labels from the excel file."""
    try:
        labels_df = pd.read_excel(file_path)
        return labels_df
    except Exception as e:
        print(f"Error loading labels file: {e}")
        return None


# # Organize audio files by labels
# def organize_audio_files(labels_df):
#     """Organize audio files into subfolders based on their labels."""
#     for index, row in labels_df.iterrows():
#         audio_path = os.path.join(Config.RAW_DATA_DIR, row['filename'])
#         label = row['label']
        
#         # Create a directory for the label if it doesn't exist
#         label_dir = os.path.join(Config.ORGANISED_DATA_DIR, label)
#         os.makedirs(label_dir, exist_ok=True)

#         # Copy the file to the corresponding label directory
#         target_path = os.path.join(label_dir, row['filename'])
#         try:
#             if os.path.exists(audio_path):
#                 shutil.copy2(audio_path, target_path)  # Copy the file
#                 print(f"Copied {audio_path} to {target_path}")
#             else:
#                 print(f"File not found: {audio_path}")
#         except Exception as e:
#             print(f"Error organizing file {audio_path}: {e}")


# Main execution
if __name__ == "__main__":
    labels_df = load_labels(Config.LABELS_FILE)
    if labels_df is not None:
        print("Labels loaded successfully.")
        
        # organize_audio_files(labels_df)
        # print("Data extraction completed: Files organized by labels.")
    else:
        print("Failed to load labels.")
