# #https://stackoverflow.com/questions/52491656/extracting-images-from-presentation-file

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pathlib import Path
from PIL import Image

class dump_pics:
    def __init__(self,filename,media_dir):
        self.filename=filename
        self.image_num = 0
        self.deck_name = filename.stem
        self.slidenum = -1
        self.media_dir = media_dir
        
    def write_image(self,shape):
        image = shape.image
        # ---get image "file" contents---
        image_bytes = image.blob
        image_type = image.ext.lower()
        # ---make up a name for the file, e.g. 'image.jpg'---
        image_filename = f'{self.deck_name}-slide_{self.slidenum}-{self.image_num:03d}.{image_type}'
        self.image_num += 1
        full_path = self.media_dir / image_filename
        with open(full_path, 'wb') as f:
            print(f"writing {str(full_path)}")
            f.write(image_bytes)
        if image_type != 'png':
            png_path = full_path.with_suffix('.png')
            print(f"need to convert {image_filename}")
            try:
                with Image.open(full_path) as im:
                    im.load()
                    im.save(png_path)
            except OSError as e:
                print(f"converion failed -- only works on windows")
                print(e)

    def visitor(self,shape):
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            print(f"in a group")
            for count,s in enumerate(shape.shapes):
                print(f"group member {count}")
                self.visitor(s)
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            print(f"individual picture")
            self.write_image(shape)

    def find_images(self):
        prs = Presentation(self.filename)
        for slidenum, slide in enumerate(prs.slides):
            self.slidenum=slidenum
            for shape in slide.shapes:
                self.visitor(shape)

if __name__ == "__main__":
    media_dir = Path('media')
    media_dir.mkdir(parents=True,exist_ok=True)
    the_files = Path().glob("*.pptx")
    for a_file in the_files:
        do_job = dump_pics(a_file,media_dir)
        do_job.find_images()
