"""
usage:

turn all docx files into markdown files

   python run_pandoc.py transform-docs
   
turn all tex files nto markdown files
   python run_pandoc.py transform-docs --doctype=tex
   
move all csv, md, pptx, docx, png, jpeg, jpg etc.
into Book/subdir folders, where subdir is the suffix filename
and write a file catlog Book/file_catalog.json

   python run_pandoc.py move-files
  
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
import copy
import json

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
       python run_pandoc.py transform-docs --doctype=tex
    \b   
    move all csv, md, pptx, docx, png, jpeg, jpg etc.
    into Book/subdir folders, where subdir is the suffix filename
    and write a file catlog Book/file_catalog.json
          python run_pandoc.py move-files
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
def move_files():
    """
    move all files with a particular suffix to Book, creating a new subfolder
    for each suffix.  Any duplicate filenames are renamed by adding an integer counter to
    the name in the form of "dup-counter"

    A json file Book/file_catalog.json is written with the filelist
    """
    all_files = list(Path().glob("**/*"))
    #
    # don't double count files in the Book directory
    #
    all_files = [item for item in all_files
                      if str(item).find("Book") == -1]
    all_files = [item for item in all_files
                      if str(item).find(".git") == -1]
    all_files = [item for item in all_files if item.suffix not in ['.docx','pptx']]
    all_files = [item for item in all_files if item.is_file()]
    all_files = [item for item in all_files if item.name[-1:] not in ['#','~']]
    all_suffixes = [item.suffix for item in all_files]
    #
    # renove duplicates
    #
    unique_suffixes = set(all_suffixes)
    #
    # remove the leading period
    #
    unique_suffixes = [item[1:] for item in unique_suffixes]
    #
    # make a subfolder to hold each suffix
    #
    Book = Path() / 'Book'
    Book.mkdir(parents=True,exist_ok=True)
    for subdir in unique_suffixes:
        new_dir = Book / subdir
        new_dir.mkdir(parents=True,exist_ok = True)
    #
    # put all files in a dictionary indexed by filename
    #
    keep_dict=defaultdict(list)
    for a_file in all_files:
        keep_dict[a_file.name].append(a_file)
    keep_dict.pop( "'.'",None)
    keep_dict.pop('.DS_Store',None)
    #
    # build a new dictionary adding
    #  unique names for any duplicates
    #
    working_dict = copy.deepcopy(keep_dict)
    bad_keys=[]
    for key,value in keep_dict.items():
        if len(value) > 1:
            for count,item in enumerate(value):
                print(f"processing duplicate name: {item}")
                new_name=f"dup-{count}-{item.name}"
                working_dict[new_name]=[item]
                bad_keys.append(key)
                count+=1
    #
    # remove the keys that had duplocate names
    #
    for key in bad_keys:
        working_dict.pop(key,None)
    out_dict = defaultdict(dict)
    for key, value in working_dict.items():
        filepath = value[0]
        #
        # drop the leading . in suffix
        #
        suffix=filepath.suffix[1:]
        out_dict[suffix][key]=str(filepath)
    #
    # convert back to ordinary dict for json
    #
    out_dict = dict(out_dict)
    pp.pprint(out_dict)
    json_file = Book / 'file_catalog.json'
    with open(json_file,'w') as outfile:
        json.dump(out_dict,outfile,indent=4)
    for key,file_dict in out_dict.items():
        write_dir = Book / key
        for unique_name, file_path in file_dict.items():
            new_path = write_dir / unique_name
            shutil.copy(file_path, new_path)
            
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
    
