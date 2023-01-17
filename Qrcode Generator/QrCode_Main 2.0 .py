import qrcode
from PIL import Image

while True:
    #list of options
    options = ['facebook', 'github', 'instagram', 'snapchat',
               'telegram', 'twitter', 'whatsapp', 'youtube']

    print("-"*40) #formatting

    usr_input = ''
    input_msg = "Please Enter an Option from below List: \n"

    #numbering the options in the list
    for index, item in enumerate(options):
        input_msg = input_msg + f'({index + 1}) {item}\n'

    input_msg += 'Your Choice: '

    while usr_input not in map(str, range(1, len(options) + 1)):
        usr_input = input(input_msg)

    print("-"*40)
    print('Your Choice for Custom Logo QRCode: ' + options[int(usr_input) - 1])

    logo_path = r"icons/"
    logo = Image.open(logo_path + usr_input + '.png')
    basewidth = 75
    wpercent = basewidth / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

    options_prompts = {'1':'Enter Your Facebook Profile URL: ',
                       '2':'Enter Your GitHub Profile URL: ',
                       '3':'Enter Your Instagram Profile URL: ',
                       '4':'Enter Your SnapChat Profile URL: ',
                       '5':'Enter Your Telegram Username: ',
                       '6':'Enter Your Twitter Profile URL: ',
                       '7':'Enter Your WhatsApp Number: ',
                       '8':'Enter Your YouTube Channel URL: '}

    options_filenames = {'1':'facebook_QrCode.png',
                         '2':'github_QrCode.png',
                         '3':'instagram_QrCode.png',
                         '4':'snapchat_QrCode.png',
                         '5':'telegram_QrCode.png',
                         '6':'twitter_QrCode.png',
                         '7':'whatsapp_QrCode.png',
                         '8':'youtube_QrCode.png'}

    prompt = options_prompts[usr_input]
    filename = options_filenames[usr_input]

    if usr_input == "1":
        fb = input(prompt)
        qr_big.add_data(fb)
    elif usr_input == "2":
        gh = input(prompt)
        qr_big.add_data(gh)
    elif usr_input == "3":
        ig = input(prompt)
        qr_big.add_data(ig)
    elif usr_input == "4":
        sc = input(prompt)
        qr_big.add_data(sc)
    elif usr_input == '5':
        print("Telegram Usernames are case sensitive.")
        te = input(prompt)
        tlgrm = 'https://t.me/' + te
        qr_big.add_data(tlgrm)
    elif usr_input == "6":
        tw = input(prompt)
        qr_big.add_data(tw)
    elif usr_input == '7':
        wp = input(prompt)
        wtsp = "http://wa.me/91" + wp
        qr_big.add_data(wtsp)
    elif usr_input == "8":
        yt = input(prompt)
        qr_big.add_data(yt)

    qr_big.make(fit=True)
    img_qr_big = qr_big.make_image(fill_color="black", back_color='white').convert("RGB")
    pos = ((img_qr_big.size[0] - logo.size[0]) // 2,
           (img_qr_big.size[1] - logo.size[1]) // 2)
    img_qr_big.paste(logo, pos)

    img_qr_big.save(filename)

    print("Qr Code Generated. And saved in the Computer")
    print("-"*40)

    repeat = input("Do you want to generate another QR code? (yes/no) ")
    if repeat.lower() == "no":
        break
