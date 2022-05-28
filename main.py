import pyotp

SECRET_KEY = pyotp.random_base32()
print(f'Secret Key: {SECRET_KEY}\n')


def validate_otp():
    print('Still Under Development')


def gen_qr_code():
    email = input('Enter Email: ')
    issuer_name = input('Enter Issuer Name: ')

    x = pyotp.totp.TOTP(SECRET_KEY).provisioning_uri(name=email, issuer_name=issuer_name)

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save("sample.png")
    qr.print_ascii()


def init():
    options = ['1', '2']
    msg_1 = 'Choose An Option\n' \
            '1: Enter OTP\n' \
            '2: Get QR Code For OTP\n'
    print(msg_1)
    entered_option = input('Enter Option: ')
    if entered_option not in options:
        print('Invalid Option Entered')
        exit()

    function_library = {
        '1': validate_otp,
        '2': gen_qr_code
    }

    function = function_library[entered_option]
    function()


init()
