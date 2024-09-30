# Document Question Answering

## Overview

This project implements a Document Question Answering (DQA) system that allows users to query information from various document types. Leveraging advanced Natural Language Processing (NLP) techniques and machine learning models, the system extracts relevant answers based on user queries from the input documents.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Format](#data-format)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extracts answers from various document types (e.g., PDFs, Word documents, etc.)
- Supports natural language queries.
- High accuracy in retrieving relevant information.
- User-friendly interface for querying documents.
- Can be integrated with other applications for seamless use.

## Technologies Used

- Python
- Natural Language Processing libraries (e.g., NLTK, SpaCy, Transformers)
- Machine Learning frameworks (e.g., TensorFlow, PyTorch)
- Document processing libraries (e.g., PyMuPDF, python-docx)
- Flask or FastAPI for the web interface

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/document-question-answering.git
   cd document-question-answering


# Missing Rent Payments Script

This script identifies missing rent payments for properties based on transaction data stored in a CSV file. It reads the rent transaction records, determines the expected payment months, and outputs any missing payments in JSON format.

## Features

- **Dynamic Date Range**: Automatically calculates the start and end dates based on the dates present in the CSV file.
- **Group by Property**: Checks for missing payments for each property separately.
- **JSON Output**: Returns the results in a clear and structured JSON format.

## Requirements

- Python 3.x
- Pandas library

You can install the required libraries using pip:

```bash
pip install pandas
```

## Usage

1. **Prepare your CSV file**: Ensure your CSV file contains a 'Date' column (formatted as YYYY-MM-DD) and a 'PropertyId' column. Example format:

   ```csv
   Date,PropertyId,Amount
   2024-01-01,1,1000
   2024-02-01,1,1000
   2024-01-01,2,1200
   ```

2. **Run the script**:

   ```bash
   python missing_rent_payments.py
   ```

   When prompted, enter the path to your rent transaction CSV file.

   ```
   Please enter the path to the rent transaction CSV file: /path/to/rent-transaction.csv
   ```

3. **Output**: The script will print a JSON representation of missing rent payments. For example:

   ```json
   [
       {
           "propertyId": 1,
           "month": "2024-03"
       },
       {
           "propertyId": 2,
           "month": "2024-02"
       }
   ]
   ```

## Functionality

The script works as follows:

1. **Load Data**: Reads the CSV file containing rent transaction records.
2. **Convert Dates**: Converts the 'Date' column to a datetime format.
3. **Determine Date Range**: Calculates the start and end dates based on the available transaction dates.
4. **Group Data**: Groups the data by `PropertyId` and `Month` to identify received payments.
5. **Find Missing Payments**: Compares received payments against the expected payment months and identifies any missing months.
6. **Output Results**: Returns the results in a structured JSON format.

## Error Handling

If there is an issue reading the CSV file, the script will return a JSON error message indicating the failure reason.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

[Your Name]  
[Your Contact Information]