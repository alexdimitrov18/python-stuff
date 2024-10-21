import qrcode
from PIL import Image, ImageDraw
import os


def generate_dot_qr_code(data, logo_path=None, save_path=None, filename="dot_qrcode.png", dot_color="black",
                         bg_color="white"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=2,  # Larger version for more data space and customization
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow the logo
        box_size=10,  # Size of each box (pixel size)
        border=4,  # Thickness of the border (in boxes)
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code but without drawing the squares
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Get the dimensions of the QR code (number of boxes)
    qr_width, qr_height = qr_img.size
    box_size = qr_width // (qr.modules_count + 2 * qr.border)  # Calculate individual box size

    # Create a blank image with background color
    dot_qr_img = Image.new("RGB", (qr_width, qr_height), bg_color)
    draw = ImageDraw.Draw(dot_qr_img)

    # Iterate through the QR code matrix and draw dots
    for row in range(qr.modules_count):
        for col in range(qr.modules_count):
            if qr.modules[row][col]:  # Check if this part of the QR code is filled (True)
                # Calculate the position to draw the dot
                x = (col + qr.border) * box_size + box_size // 2
                y = (row + qr.border) * box_size + box_size // 2

                # Draw a thicker circle (dot) instead of a square
                radius = box_size // 1.9  # Increase radius to make the dots thicker
                draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=dot_color)

    # If a logo path is provided, embed the logo in the middle of the QR code
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)

        # Resize the logo to fit into the center of the QR code (20-30% of the QR code size)
        logo_size = int(qr_width * 0.25)  # Logo size is set to 25% of the QR code width
        logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

        # Calculate the position to place the logo (centered on the QR code)
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste the logo onto the QR code (transparent if PNG)
        dot_qr_img.paste(logo, logo_pos, mask=logo)  # The mask ensures transparency

    # If a save path is provided, save to that path, otherwise save to the current directory
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, filename)
    else:
        file_path = filename

    # Save the image to the specified file
    dot_qr_img.save(file_path)
    print(f"Dot QR code saved as {file_path}")


# Example usage
data = "https://www.instagram.com/nbu_hiking.corner/"
logo_path = r"C:\Users\Alex\Downloads\logo2.png"  # Path to the logo you provided
save_path = r"C:\Users\Alex\Downloads"  # Directory where you want to save the QR code
generate_dot_qr_code(data, logo_path=logo_path, save_path=save_path, filename="dot_qrcode_with_logo.png",
                     dot_color="green", bg_color="white")
