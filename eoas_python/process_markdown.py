from pathlib import Path
import copy
all_files = list((Path() / "book/docs").glob("*.md"))


def rewrite_file(file_path):
    with open(file_path,'r',encoding="utf8") as infile:
        all_lines = list(infile.readlines())
    with open(file_path,'w',encoding="utf8",
              errors="replace") as out:
        for a_line in all_lines:
            new_line = copy.copy(a_line)
            if a_line.find('θ') > -1:
                print(f'hit it with {a_line}')
                new_line=a_line.replace('θ','theta')
            out.write(new_line)

for a_file in all_files:
    print(a_file)
    rewrite_file(a_file.resolve())

