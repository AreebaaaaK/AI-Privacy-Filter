import re

def detect_sensitive_data(data):

    sensitive_indices = []

    combined_text = " ".join(data['text'])

    phone_pattern = r'(\+91[\s-]?)?[6-9]\d{9}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    upi_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z]+'

    bank_account_pattern = r'\b\d{9,18}\b'
    card_pattern = r'\b\d{16}\b'
    ifsc_pattern = r'[A-Z]{4}0[A-Z0-9]{6}'

    aadhaar_pattern = r'\b\d{4}\s?\d{4}\s?\d{4}\b'
    pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'

    transaction_pattern = r'pay_[A-Za-z0-9]+'
    generic_id_pattern = r'[A-Za-z0-9]{10,}'

    otp_pattern = r'\b\d{4,6}\b'

    matches = []

    matches += re.findall(phone_pattern, combined_text)
    matches += re.findall(email_pattern, combined_text)
    matches += re.findall(upi_pattern, combined_text)

    matches += re.findall(bank_account_pattern, combined_text)
    matches += re.findall(card_pattern, combined_text)
    matches += re.findall(ifsc_pattern, combined_text)

    matches += re.findall(aadhaar_pattern, combined_text)
    matches += re.findall(pan_pattern, combined_text)

    matches += re.findall(transaction_pattern, combined_text)
    matches += re.findall(generic_id_pattern, combined_text)

    matches += re.findall(otp_pattern, combined_text)

    for i, word in enumerate(data['text']):
        for match in matches:
            if match and match.replace(" ", "") in word.replace(" ", ""):
                sensitive_indices.append(i)

    return list(set(sensitive_indices))