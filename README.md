# DiagnosCode

Automating medical coding from inpatient records using AI/ML.

## Project Overview

DiagnosCode is a project aimed at automating the process of medical coding from inpatient records. By leveraging machine learning and natural language processing (NLP), DiagnosCode reads doctors' notes and medical records to generate accurate medical codes for insurance billing.

## Features

- **OCR Integration**: Converts scanned documents and handwritten notes into digital text.
- **NLP Processing**: Extracts key information such as diagnoses, treatments, and symptoms from text.
- **Machine Learning Models**: Predicts the appropriate medical codes based on the extracted information.
- **Scalability**: Designed to handle large volumes of medical records efficiently.
- **Deployment Ready**: Includes tools for containerization and deployment.

## Setup Instructions

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Anaconda (Optional but recommended)](https://www.anaconda.com/products/distribution)
- [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/)

### Repository Clone

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/DiagnosCode.git
    cd DiagnosCode
    ```

### Virtual Environment Setup

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1   # For PowerShell on Windows
    # source venv/bin/activate    # For macOS/Linux
    ```

### Install Dependencies

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Directory Structure

The project directory structure is organized as follows:

DiagnosCode/
├── .gitignore
├── LICENSE
├── README.md
├── data/
│ ├── raw/
│ ├── processed/
├── models/
├── notebooks/
├── src/
│ ├── init.py
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── inference.py
├── requirements.txt
└── venv/


### Running the Project

4. **Data Preprocessing**:
    ```bash
    python src/data_preprocessing.py
    ```

5. **Model Training**:
    ```bash
    python src/model_training.py
    ```

6. **Inference**:
    ```bash
    python src/inference.py
    ```

## Usage

- **Data Preprocessing**: Script to clean and preprocess medical records.
- **Model Training**: Train machine learning models on preprocessed data.
- **Inference**: Generate medical codes from new inpatient records.

## Contributing

We welcome contributions to DiagnosCode. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [Vishal R Chandupatla](mailto:aiforu507@gmail.com.com or vishal.reddy.1398@gmail.com).

