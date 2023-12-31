import os
from PIL import Image
from flask import url_for, current_app

def addChannelLogo(pic_upload, channelName):

    filename = pic_upload.filename
    
    ext_type = filename.split('.')[-1]
    storage_filename = str(channelName) + '.' + ext_type
    filepath = os.path.join(current_app.root_path, 'static\channelsLogo', storage_filename)

    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename