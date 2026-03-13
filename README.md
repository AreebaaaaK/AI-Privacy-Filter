# AI Privacy Filter

AI Privacy Filter is a cybersecurity tool that automatically detects and protects sensitive information in images and screenshots. The system uses **Optical Character Recognition (OCR)** and pattern detection to identify personal data such as phone numbers, emails, bank details, Aadhaar numbers, and more. Sensitive regions are automatically blurred to prevent information leakage.

---

## Features

- Automatic screenshot monitoring  
- Detection of sensitive data using OCR and regex patterns  
- Blurring of confidential information in images  
- Web interface for manual image upload and processing  
- Real-time monitoring of screenshot folder using Watchdog  
- Supports detection of multiple types of personal data  

---

## Technologies Used

- Python  
- OpenCV  
- Tesseract OCR  
- Flask  
- Watchdog  
- NumPy  
- Regular Expressions (Regex)

---

## System Workflow

1. User captures a screenshot or uploads an image.
2. The system monitors the screenshot folder using Watchdog.
3. The image is processed using Tesseract OCR to extract text and coordinates.
4. Regex patterns detect sensitive information such as phone numbers, Aadhaar numbers, emails, etc.
5. OpenCV blurs the detected sensitive regions.
6. A protected version of the image is saved automatically.

---

## Detected Sensitive Data

The system detects several types of confidential information including:

- Phone Numbers  
- Email Addresses  
- Aadhaar Numbers  
- PAN Numbers  
- Bank Account Numbers  
- Credit/Debit Card Numbers  
- IFSC Codes  
- UPI IDs  
- OTP Codes  
- Transaction IDs  

---

## Project Structure


AI-Privacy-Filter
│
├── app.py # Flask web interface
├── background_watcher.py # Automatic screenshot monitoring
├── privacy_engine.py # OCR processing and image protection
├── detector.py # Sensitive data detection logic
├── requirements.txt # Required Python libraries
└── README.md # Project documentation


---

## Installation

Clone the repository:

```bash
git clone https://github.com/AreebaaaaK/AI-Privacy-Filter.git
cd AI-Privacy-Filter

Create a virtual environment:

python -m venv venv

Activate the environment:

venv\Scripts\activate

Browser extension for screenshot protection
Install dependencies:

pip install -r requirements.txt

Install Tesseract OCR and set its path inside privacy_engine.py.

