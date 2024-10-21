import qrcode
from PIL import Image
import os


def generate_qr_code_with_logo(data, logo_path=None, save_path=None, filename="qrcode_with_logo.png"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=2,  # controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction for logo
        box_size=15,  # size of each box (pixel size)
        border=5,  # thickness of the border (in boxes)
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # If a logo path is provided, embed the logo in the middle of the QR code
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)

        # Calculate the size of the logo (20% of the QR code size)
        qr_width, qr_height = qr_img.size
        logo_size = int(qr_width * 0.2)  # Logo size will be 20% of the QR code width

        # Resize the logo while maintaining aspect ratio
        logo.thumbnail((logo_size, logo_size))

        # Calculate position to place the logo (center of the QR code)
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste the logo onto the QR code
        qr_img.paste(logo, logo_pos, mask=logo)

    # If a save path is provided, save to that path, otherwise save to the current directory
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, filename)
    else:
        file_path = filename

    # Save the image to the specified file
    qr_img.save(file_path)
    print(f"QR code with logo saved as {file_path}")


# Example usage
data = "https://www.instagram.com/nbu_hiking.corner/"
logo_path = r"C:\Users\Alex\Downloads\logo2.png"  # Path to your logo file
save_path = r"C:\Users\Alex\Downloads"  # Directory where you want to save the QR code
generate_qr_code_with_logo(data, logo_path=logo_path, save_path=save_path, filename="QR_with_logo.png")
