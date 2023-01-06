#importing necessary modules
import qrcode
from PIL import Image

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


logo = Image.open(r"/home/gedion/PycharmProjects/QRcode Generator/icons/" + usr_input + '.png')
basewith = 75
wpercent = basewith/float(logo.size[0])
hsize = int((float(logo.size[1] * float(wpercent))))
logo = logo.resize((basewith, hsize), Image.Resampling.LANCZOS)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)


def url():
    ''' function to  take user input for selected logo'''
    if usr_input == "1":    #this "1" in quotes becz the user input is string
        fb = input("Enter Your Facebook Profile URL: ")
        qr_big.add_data(fb)
        return fb

    elif usr_input == "2":
        gh = input("Enter Your GitHub Profile URL: ")
        qr_big.add_data(gh)
        return gh

    elif usr_input == "3":
        ig = input("Enter Your Instagram Profile URL: ")
        qr_big.add_data(ig)
        return ig

    elif usr_input == "4":
        sc = input("Enter Your SnapChat Profile URL: ")
        qr_big.add_data(sc)
        return sc

    elif usr_input == '5':
        print("Telegram Usernames are case sensitive.")
        te = input("Enter Your Telegram Username: ")
        tlgrm = 'https://t.me/' + te
        qr_big.add_data(tlgrm)
        return tlgrm

    elif usr_input == "6":
        tw = input("Enter Your Twitter Profile URL: ")
        return tw

    elif usr_input == '7':
        wp = input("Enter Your WhatsApp Number: ")
        wtsp = "http://wa.me/91" + wp
        qr_big.add_data(wtsp)
        return wtsp

    elif usr_input == "8":
        yt = input("Enter Your YouTube Channel URL: ")
        qr_big.add_data(yt)
        return yt

url()


qr_big.make(fit=True)
img_qr_big = qr_big.make_image(fill_color="black", back_color='white').convert("RGB")
pos = ((img_qr_big.size[0] - logo.size[0]) // 2,
       (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)


'''rename & save file acc to chosen logo'''

if usr_input == "1":
    img_qr_big.save('facebook_QrCode.png')

elif usr_input == "2":
    img_qr_big.save('github_QrCode.png')

elif usr_input == "3":
    img_qr_big.save('instagram_QrCode.png')

elif usr_input == "4":
    img_qr_big.save('snapchat_QrCode.png')

elif usr_input == "5":
    img_qr_big.save('telegram_QrCode.png')

elif usr_input == "6":
    img_qr_big.save('twitter_QrCode.png')

elif usr_input == "7":
    img_qr_big.save('whatsApp_QrCode.png')

elif usr_input == "8":
    img_qr_big.save('YouTube_QrCode.png')

print("-"*40)
print("Your Custom Logo QR code Generated.")
print("-"*40)




