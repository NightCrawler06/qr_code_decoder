import tkinter as tk
from tkinter import filedialog, messagebox
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageTk


class QRCodeDecoderApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Decoder")
        master.geometry("600x500")


        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)


        self.image_frame = tk.Frame(self.main_frame, width=500, height=300,
                                    relief=tk.SUNKEN, borderwidth=2)
        self.image_frame.pack(pady=10)
        self.image_frame.pack_propagate(False)

        self.image_label = tk.Label(self.image_frame, text="No image selected")
        self.image_label.pack(expand=True, fill=tk.BOTH)


        self.data_text = tk.Text(self.main_frame, height=5, width=50, wrap=tk.WORD)
        self.data_text.pack(pady=10)
        self.data_text.config(state=tk.DISABLED)


        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)


        self.select_button = tk.Button(self.button_frame,
                                       text="Select Image",
                                       command=self.select_image)
        self.select_button.pack(side=tk.LEFT, padx=10)


        self.decode_button = tk.Button(self.button_frame,
                                       text="Decode QR Code",
                                       command=self.decode_qr_code,
                                       state=tk.DISABLED)
        self.decode_button.pack(side=tk.LEFT, padx=10)


        self.file_path = None
        self.current_image = None

    def select_image(self):

        self.file_path = filedialog.askopenfilename(
            title="Select QR Code Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )


        if self.file_path:
            try:

                original_image = Image.open(self.file_path)


                frame_width = self.image_frame.winfo_width()
                frame_height = self.image_frame.winfo_height()


                original_image.thumbnail((frame_width, frame_height), Image.LANCZOS)


                self.current_image = ImageTk.PhotoImage(original_image)


                self.image_label.config(image=self.current_image, text="")


                self.decode_button.config(state=tk.NORMAL)

            except Exception as e:
                messagebox.showerror("Error", f"Could not open image: {str(e)}")

    def decode_qr_code(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select an image first.")
            return

        try:
            # Open the image
            image = Image.open(self.file_path)

            # Decode QR codes
            qr_codes = pyzbar.decode(image)


            self.data_text.config(state=tk.NORMAL)
            self.data_text.delete(1.0, tk.END)

            if not qr_codes:
                self.data_text.insert(tk.END, "No QR code found in the image.")
            else:
                # Display QR code data
                for i, barcode in enumerate(qr_codes, 1):
                    decoded_data = barcode.data.decode('utf-8')
                    self.data_text.insert(tk.END, f"QR Code {i}: {decoded_data}\n")

            self.data_text.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Error", f"Error decoding QR code: {str(e)}")


def main():
    root = tk.Tk()
    app = QRCodeDecoderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()