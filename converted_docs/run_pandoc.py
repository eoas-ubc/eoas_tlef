"""
usage:

turn all docx files into markdown files
   python run_pandoc.py transform-docs
turn all tex files nto markdown files
   python run_pandoc.py transform-docs --doctype=texp
remove all media files
   python run_pandoc.py clean-media
remove all markdown files
   python run_pandoc clean-markdown
"""
import contextlib
import os, sys
from pathlib import Path
import subprocess
import pprint
import shutil
import click
from collections import defaultdict

pp=pprint.PrettyPrinter(indent=4)

@contextlib.contextmanager
def cd(path):
    print(f'initially inside {os.getcwd()}')
    CWD = os.getcwd()
    os.chdir(path)
    print(f'inside {os.getcwd()}')
    try:
        yield
    except Exception as e:
        print(f'Exception caught: {e}')
    finally:
        print(f'finally inside {os.getcwd()}')
        os.chdir(CWD)

@click.group()
def main():
    """\b
    usage: \b
    \b
    to turn all docx files into markdown files\b
       python run_pandoc.py transform-docs
    \b
    to turn all tex files nto markdown files\b
       python run_pandoc.py transform-docs --doctype=texp
    \b
    to remove all media files\b
       npython run_pandoc.py clean-media
    \b
    to remove all markdown files\b
       python run_pandoc clean-markdown
    """
    pass

@main.command()
def clean_media():
    all_media_dirs = Path().glob("**/*media*")
    all_list = []
    for a_dir in all_media_dirs:
        if a_dir.is_dir():
            all_list.append(str(a_dir))
    bad_dirs = pp.pformat(all_list)
    print(f"preparing to remove:\n{bad_dirs}")
    for item in all_list:
        try:
            shutil.rmtree(item)
        except FileNotFoundError:
            pass

@main.command()
def move_markdown():
    """
    move all markdown files and figures into a book folder
    """
    keep_dict=defaultdict(list)
    md_files = list(Path().glob("**/*.md"))
    Book = Path() / 'Book'
    Book.mkdir(parents=True,exist_ok=True)
    for the_file in md_files:
        keep_dict[the_file.name].append(the_file)
    for key,value in keep_dict.items():
        print(key,value)
        if len(value) > 1:
            raise ValueError(f'more than 1 file: {value}')
        shutil.copy(value[0],Book)
    # md_files = Path().glob("**/*.m")
    # Book = Path() / 'Book'
    # Book.mkdir(parents=True,exist_ok=True)
    # for item in md_files:
    #     shutil.copy(item,Book)
    # print(all_suffixes)
    # fig_list=['.png', '.pdf', 'jpeg','jpg']
        
    
        
@main.command()
def clean_markdown():
    all_markdown_files = Path().glob("**/*.md")
    all_list = []
    for a_file in all_markdown_files:
        if a_file.is_file():
            all_list.append(str(a_file))
    bad_files = pp.pformat(all_list)
    print(f"preparing to remove:\n{bad_files}")
    for item in all_list:
        try:
            os.remove(item)
        except FileNotFoundError:
            pass

@main.command()
@click.option('--doctype', default="docx", show_default=True)
def transform_docs(doctype):
    """\b
    doctype can be either docx or tex\b
    default value is docx\b
    """
    docx_files = Path().glob(f"**/*.{doctype}")
    for a_file in docx_files:
        the_dir = a_file.parent
        #
        # change into the directory to execute pandoc, returning
        # to the run directory once the command completes or if
        # there is an exception
        #
        with cd(the_dir):
            in_name = Path(a_file.name)
            out_name = f"--output={in_name.with_suffix('.md')}"
            media_dir = f"--extract-media={in_name.stem}_figs"
            arglist=["pandoc", "--to", "gfm", media_dir,
                                     out_name,a_file.name]
            print(f"running the command \n{' '.join(arglist)}\n")
            result = subprocess.run(arglist, capture_output=True)
            if result.stdout:
                print('output: ',result.stdout)
            if result.stderr:
                print('error: ',result.stderr)


if __name__ == "__main__":
    main()
    
