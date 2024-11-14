import qrcode

def genereteQRcode(data):
    
    # Generisanje QR koda
    qr = qrcode.QRCode(
        version=1,  # verzija QR koda (1 je za male veličine, veći broj za veće veličine)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # veličina jednog kvadrata u QR kodu
        border=4,  # širina okvira QR koda
    )

    # Dodavanje podataka u QR kod
    qr.add_data(data)
    qr.make(fit=True)

    # Kreiranje slike QR koda
    img = qr.make_image(fill_color="black", back_color="white")

    # Čuvanje slike
    img.save("qrcode.png")
    print("QR kod je sačuvan kao 'qrcode.png'")


data = "mire"
genereteQRcode(data)

