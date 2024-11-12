import barcode
from barcode.writer import ImageWriter

def generateBarcode(data):
    # Create a barcode object using EAN-13 format and ImageWriter for creating an image
    barcode_class = barcode.get_barcode_class('ean13')
    barcode_instance = barcode_class(barcode_data, writer=ImageWriter())

    # Save the barcode as an image file (e.g., PNG)
    barcode_instance.save('barcode image ' + data)

    print("Barcode generated and saved as 'barcode_image.png'")


# Define the barcode data (e.g., a product ID or any string of digits)
barcode_data = "123123123123"  # This can be any string, like a UPC or EAN
generateBarcode(barcode_data)
