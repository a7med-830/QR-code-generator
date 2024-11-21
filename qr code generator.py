import qrcode
import qrcode.image.svg
import time

def qr_gen(qr, img_name, fill_color, back_color):
    print("What type do you want to save as?")
    print("[1] Pixels (PNG)")
    print("[2] Vector (SVG)")
    print("[3] Both")
    file_type = input("Enter your choice: ")

    if file_type == "1":
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(f"{img_name}.png")
        print(f"QR Code saved as {img_name}.png")

    elif file_type == "2":
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
        img.save(f"{img_name}.svg")
        print(f"QR Code saved as {img_name}.svg")

    elif file_type == "3":
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(f"{img_name}.png")
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
        img.save(f"{img_name}.svg")
        print(f"QR Code saved as {img_name}.png and {img_name}.svg")

    else:
        print("Invalid choice. No file saved.")


print("QR Code Generator by Ahmed EL-Shekih")
is_running = True

while is_running:
    text = input("Enter your text/URL: ")

    try:
        size = int(input("Choose the size of the QR Code (1–40): "))
        if not (1 <= size <= 40):
            raise ValueError("Size must be between 1 and 40.")

        border_size = int(input("Choose the thickness of the border (0–40): "))
        if not (0 <= border_size <= 40):
            raise ValueError("Border size must be between 0 and 40.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue

    fill_color = input("Choose a fill color (name or hex code): ")
    back_color = input("Choose a background color (name or hex code): ")

    qr = qrcode.QRCode(
        version=size,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10, 
        border=border_size,  
    )
    qr.add_data(text)
    qr.make()

  
    img_name = input("Enter a name for the QR image (without extension): ")

    qr_gen(qr, img_name, fill_color, back_color)

    if input("Do you want to create another one? [y/n]: ").lower() == "n":
        is_running = False

print("Exiting in 5 seconds...")
time.sleep(5)
