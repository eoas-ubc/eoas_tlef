# based on https://stackoverflow.com/questions/52491656/extracting-images-from-presentation-file
import click
import context
from pathlib import Path
from convert_lib.core_funs import Extract_Pics

@click.command()
@click.argument("pptx_file", type=str, nargs=1)
@click.argument("media_directory", type=str, nargs=1)
def main(pptx_file, media_directory):
    """\b
    usage: python image_extract.py pptx_file media_directory
    pptx_file: powerpoint file to convert
    media_directory: folder of png files to hold images from pptx
    """
    media_dir = Path(media_directory)
    media_dir.mkdir(parents=True,exist_ok=True)
    pptx_file = Path(pptx_file)
    do_job = Extract_Pics(pptx_file,media_dir)
    do_job.find_images()

                
if __name__ == "__main__":
    main()
