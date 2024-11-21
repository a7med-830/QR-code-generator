import qrcode
import qrcode.image.svg

def get_data(qr):
    text = input("Enter your text/URL: ")
    qr.add_data(text)

# Create QRCode object
qr = qrcode.QRCode()

# Get user data
get_data(qr)

# Prompt for image name
img_name = input("Enter a name for the QR image (without extension): ")

# Generate the QR code
qr.make()

# Ask the user for the type of file to save
file_type = input("What type do you want to save as?\n[1] Pixels (PNG)\n[2] Vector (SVG)\nEnter your choice: ")

if file_type == '1':
    # Save as a pixel-based PNG image
    img = qr.make_image()
    img.save(f"{img_name}.png")
    print(f"QR Code saved as {img_name}.png")

elif file_type == '2':
    # Save as a vector-based SVG image
    img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
    img.save(f"{img_name}.svg")
    print(f"QR Code saved as {img_name}.svg")

else:
    print("Invalid choice. No file saved.")
