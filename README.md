# Convolutional Neural Network for Whale Sound Classification

This repository contains a deep learning project designed to classify whale sounds using Convolutional Neural Networks (CNNs). The project involves creating five binary CNN models to classify five different whale species—humpback, fin, minke, omura, and downchirps from an unrecognized whale species—and a multi-class CNN model to classify all five species in a single framework.

---

## TODO
## Project Structure

```
Humpback-Whale-Classification/
├── data_extraction/
│   ├── extract_data.py
│   ├── config_file.py
├── data_preprocessing/
│   ├── preprocess_data.py
├── model/
│   ├── train_model.py
│   ├── evaluate_model.py
├── data/
│   ├── raw/
│   ├── organised/
│   ├── spectrograms/
├── environment.yml
├── README.md
```

### Key Components:
1. **`data_extraction/`**: Contains scripts for organizing and extracting raw data.
   - `extract_data.py`: Script for copying audio files into label-based directories.
   - `config_file.py`: Stores configurations like file paths.

2. **`data_preprocessing/`**: Handles the preprocessing of audio data, including converting `.wav` files to spectrogram images.

3. **`model/`**: Scripts for training, testing, and evaluating the CNN model.

4. **`data/`**: Directory for raw data, organized data, and generated spectrograms.

5. **`environment.yml`**: Specifies the Conda environment for the project.

6. **`README.md`**: Documentation for the repository.

---

## TODO
## Setup Instructions

### Prerequisites:
1. **Python 3.8 or later**
2. **Conda**
3. Basic knowledge of Python and Deep Learning

### TODO
### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/Humpback-Whale-Classification.git
   cd Humpback-Whale-Classification
   ```

2. Create the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate whale-classification
   ```

3. Verify dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

---

#TODO
## Usage

### Data Extraction
To organize raw data into labeled directories:
```bash
python data_extraction/extract_data.py
```
Ensure that paths in `config_file.py` are correctly set.

### Data Preprocessing
To generate spectrograms from `.wav` files:
```bash
python data_preprocessing/preprocess_data.py
```

### Model Training
To train the CNN model:
```bash
python model/train_model.py
```

### Model Evaluation
To evaluate the model's performance:
```bash
python model/evaluate_model.py
```

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## TODO
## Acknowledgements
- [Librosa](https://librosa.org/): For audio analysis.
- [TensorFlow](https://www.tensorflow.org/): For deep learning framework.
- Whale dataset courtesy of [Organization/Source].

