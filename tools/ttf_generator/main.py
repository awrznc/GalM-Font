import re
import os
import glob
import fontforge

TARGET: str = f'{ os.path.split(__file__)[0] }/../../svg'
familynames: str = glob.glob(f'{TARGET}/*')
familynames_size: int = len(familynames)

for familyname_index, familyname_path in enumerate( familynames ):

    familyname = familyname_path.split('/')[-1]

    # create new font
    font = fontforge.font()

    # set information
    font.encoding = 'unicode'
    font.version = '1.0.0'
    font.copyright = 'awrznc'
    font.fontname = 'GalM'
    font.familyname = familyname
    font.fullname = f'{font.fontname}-{font.familyname}'
    font.comment = 'This font is public domain.'
    font.fontlog = font.comment

    print(f'[{familyname_index + 1}/{familynames_size}] generate {font.fullname}')

    # add charactor
    for file in glob.glob(f'{TARGET}/{familyname}/*.svg'):
        charactor: str = os.path.split( file )[1].split('.')[0]
        glyph = font.createChar( ord(charactor), charactor )
        glyph.importOutlines( file )
        glyph.width = 1000
        glyph.vwidth = glyph.width
        # glyph.left_side_bearing = 100
        # glyph.right_side_bearing = 100

    # create truetype file
    font.save(f'{os.getcwd()}/GalM-Font/sfd/{font.fullname}.sfd')
    font.generate(f'{os.getcwd()}/GalM-Font/ttf/{font.fullname}.ttf')
