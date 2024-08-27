import sys
import pyzbar.pyzbar as pyzbar
from PIL import Image

def decode_qr_code(file_path):
    image = Image.open(file_path)
    qr_code = pyzbar.decode(image)
    if not qr_code:
        print("No QR code found in the provided image.")
        return
    for barcode in qr_code:
        print(f"Ito ung data: {barcode.data.decode('utf-8')}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qr_code_decoder.py <qr_code_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    decode_qr_code(file_path)
