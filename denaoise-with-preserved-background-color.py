import pytesseract 

import numpy as np
from scipy import signal, ndimage
from PIL import Image
from pdf2image import convert_from_path

def load_im(path):
    return np.asarray(Image.open(path))/255.0

def save(path, img):
    tmp = np.asarray(img*255.0, dtype=np.uint8)
    Image.fromarray(tmp).save(path)

def denoise_im_with_back(inp):
    # estimate 'background' color by a median filter
    bg = signal.medfilt2d(inp, 11)
    save('background.png', bg)

    # compute 'foreground' mask as anything that is significantly darker than
    # the background
    mask = inp < bg - 0.1    
    save('foreground_mask.png', mask)
    back = np.average(bg);
    
    mod = ndimage.filters.median_filter(mask,2);
    mod = ndimage.grey_closing(mod, size=(2,2));
       
    # either return forground or average of background
       
    out = np.where(mod, inp, back)  ## 1 is pure white    
    return out;

##pages = convert_from_path('test.pdf')
##for page in pages:
##    page.save('out.png', 'PNG')

inp_path = '60.png'
out_path = 'output.png'
#inp_path = 'out.png'
#inp_path = 'abc/test.pdf/0_test.pdf.jpg'

inp = load_im(inp_path)
out = denoise_im_with_back(inp)

save(out_path, out)

pytesseract.pytesseract.tesseract_cmd = r"H:\Tesseract-OCR\tesseract.exe"
print (pytesseract.image_to_string(Image.open('output.png')))
#print (pytesseract.image_to_string(Image.open('output.jpg'), lang='eng'))
