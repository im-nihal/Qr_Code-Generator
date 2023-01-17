import qrcode
from PIL import Image

# Dictionary to map user's selection to prompt for input
options_prompts = {
    'facebook': 'Enter Your Facebook Profile URL: ',
    'github': 'Enter Your GitHub Profile URL: ',
    'instagram': 'Enter Your Instagram Profile URL: ',
    'snapchat': 'Enter Your SnapChat Profile URL: ',
    'telegram': 'Enter Your Telegram Username: ',
    'twitter': 'Enter Your Twitter Profile URL: ',
    'whatsapp': 'Enter Your WhatsApp Number: ',
    'youtube': 'Enter Your YouTube Channel URL: '
}

# Dictionary to map user's selection to filename
options_filenames = {
    'facebook': 'facebook_QrCode.png',
    'github': 'github_QrCode.png',
    'instagram': 'instagram_QrCode.png',
    'snapchat': 'snapchat_QrCode.png',
    'telegram': 'telegram_QrCode.png',
    'twitter': 'twitter_QrCode.png',
    'whatsapp': 'whatsapp_QrCode.png',
    'youtube': 'youtube_QrCode.png'
}

logo_path = r"icons/"

#
def generate_qr_code(url):
    qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr_big.add_data(url)
    qr_big.make(fit=True)
    img_qr_big = qr_big.make_image(fill_color="black", back_color='white').convert("RGB")
    return img_qr_big

print("-"*40) # formatting

usr_input = ''
input_msg = "Please Enter an Option from below List: \n"


# Numbering the options in the list
for index, item in enumerate(options_prompts.keys()):
    input_msg = input_msg + f'({index + 1}) {item}\n'

input_msg += 'Your Choice: '

repeat = 'y'
while repeat == 'y':
    usr_input = ''
    while usr_input not in map(str, range(1, len(options_prompts) + 1)):
        usr_input = input(input_msg)

    print("-" * 40)
    print('Your Choice for Custom Logo QRCode: ' + str(usr_input))

    logo = Image.open(logo_path + usr_input + '.png')
    base_width = 75
    wpercent = base_width / float(logo.size[0])
    hsize = int((float(logo.size[1] * float(wpercent))))
    logo = logo.resize((base_width, hsize), Image.Resampling.LANCZOS)

    # Get the URL for the selected option and generate QR code only if user wants to continue
    usr_input = int(usr_input)
    prompt = options_prompts[list(options_prompts.keys())[usr_input - 1]]
    if repeat == 'y':
        url = input(prompt)
        img_qr_big = generate_qr_code(url)
        pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
        img_qr_big.paste(logo, pos)
        filename = options_filenames[list(options_filenames.keys())[usr_input - 1]]
        img_qr_big.save(filename)
        print(f'Your QR Code has been saved as {filename}')
        print("-" * 40)

    # Ask the user a choice to continue
    repeat = input("Do you want to generate another QR code? (y/n)")
    if repeat == 'n':
        break
    print("-" * 40)

print("I Hope You Liked Qr Code Generator")

logo = Image.open(logo_path + str(usr_input) + '.png')
base_width = 75
wpercent = base_width / float(logo.size[0])
hsize = int((float(logo.size[1] * float(wpercent))))
logo = logo.resize((base_width, hsize), Image.Resampling.LANCZOS)


img_qr_big = generate_qr_code(url)
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)

# Save the QR code with the custom logo
filename = options_filenames[list(options_filenames.keys())[usr_input -1]]
img_qr_big.save(filename)
