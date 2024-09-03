# QR Code Decoder

A simple Python script to decode QR codes from image files. This tool extracts the encoded information from a given QR code image and displays it in a human-readable format.

## Installation and Usage

To get started:

1. Clone the repository:
    ```bash
    git clone https://github.com/NightCrawler06/qr-code-decoder.git
    cd qr-code-decoder
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Decode a QR code by running:
    ```bash
    python qr_code_decoder.py <qr_code_file>
    ```
    Replace `<qr_code_file>` with the path to your QR code image file. For example:
    ```bash
    python qr_code_decoder.py sample_qr.png
    ```
    This command will output the decoded information from the QR code.

## Requirements

- Python 3.x
- `qrcode` library (install via `pip install qrcode`)
- Other dependencies listed in `requirements.txt`
