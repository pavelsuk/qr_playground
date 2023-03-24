# Source: https://proxyroot.com/vr-card-to-qr-code/

import qrcode

template = """BEGIN:VCARD
VERSION:4.0
N:{last_name};{first_name};;{name_prefix}.;
ORG:{company}
TITLE:{title}
PHOTO;MEDIATYPE#image/gif:{image_url}
TEL;TYPE#work,voice;VALUE#uri:tel:{work_phone}
TEL;TYPE#home,voice;VALUE#uri:tel:{home_phone}
ADR;TYPE#WORK;PREF#1;LABEL#"{work_address_label}":;;{work_address_line_1};{work_address_city};{work_address_stage_code};{work_address_pin};{work_address_country}
ADR;TYPE#HOME;LABEL#"{home_address_label}":;;{home_address_line_1};{home_address_city};{home_address_stage_code};{home_address_pin};{home_address_country}
EMAIL:{email}
REV:20080424T195243Z
x-qq:21588891
END:VCARD"""

"""
# from https://gist.github.com/gerwin3/ef9ae04d2b156c405db45dc70b93f716
return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
    ]
"""



details = {
    "last_name": "Khan",
    "first_name": "Afroze",
    "name_prefix": "Mr.",
    "company": "proxyroot",
    "title": "Engineering Leader",
    "image_url": "https://proxyroot.com",
    "work_phone": "+1-917-000-0000",
    "home_phone": "+1-917-000-0001",
    "work_address_label": "proxyroot",
    "work_address_line_1": "proxyroot inc",
    "work_address_city": "Azgard City",
    "work_address_stage_code": "AZ",
    "work_address_pin": "00000",
    "work_address_country": "Azgard",
    "home_address_label": "Holmes",
    "home_address_line_1": "221B Baker Street",
    "home_address_city": "London",
    "home_address_stage_code": "11111",
    "home_address_pin": "NW1 6XE",
    "home_address_country": "United Kingdom",
    "email": "afroze@proxyroot.com",
    "position": "Master of QR Codes",
    "note": "Author of the example"
}

template_mini = """BEGIN:VCARD
VERSION:4.0
N:{last_name};{first_name}
FN:{first_name} {last_name}
ORG:{company}
EMAIL:{email}
TITLE:{position}
NOTE: {note}
END:VCARD"""

details_mini = {
    "last_name": "Kan Ban",
    "first_name": "Scrumatha",
    "company": "Keep It Simple Stupid, Ltd",
    "position": "Agile Coach",
    "email": "scrumatha@kiss.in",
    "note": "Agile Conference 2024"
}

def create_qr_code_image(qr_code_data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(qr_code_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

data = template.format(**details)
# 'BEGIN:VCARD\nVERSION:4.0\nN:Khan;Afroze;;Mr..;\nORG:proxyroot\nTITLE:Engineering Leader\nPHOTO;MEDIATYPE#image/gif:https://proxyroot.com\nTEL;TYPE#work,voice;VALUE#uri:tel:+1-917-000-0000\nTEL;TYPE#home,voice;VALUE#uri:tel:+1-917-000-0001\nADR;TYPE#WORK;PREF#1;LABEL#"proxyroot":;;proxyroot inc;Azgard City;AZ;00000;Azgard\nADR;TYPE#HOME;LABEL#"Holmes":;;221B Baker Street;London;11111;NW1 6XE;United Kingdom\nEMAIL:afroze@proxyroot.com\nREV:20080424T195243Z\nx-qq:21588891\nEND:VCARD'

create_qr_code_image(data, "my-vrcard-qr-code.png")

data_mini = template_mini.format(**details_mini)
create_qr_code_image(data_mini, "my-vrcard-qr-code-mini.png")


