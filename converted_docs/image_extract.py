# based on https://stackoverflow.com/questions/52491656/extracting-images-from-presentation-file
import click
import context
from pathlib import Path
from convert_lib.core_funs import Extract_Pics, extract_it

@click.command()
@click.argument("pptx_file", type=str, nargs=1)
@click.argument("media_directory", type=str, nargs=1)
def main(pptx_file, media_directory):
    """\b
    usage: python image_extract.py pptx_file media_directory
    pptx_file: powerpoint file to convert
    media_directory: folder of png files to hold images from pptx
    """
    extract_it(pptx_file, media_directory)

                
if __name__ == "__main__":
    main()
