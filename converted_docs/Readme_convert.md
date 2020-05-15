# converting docx, tex and pptx to markdown

## docx

`conda install pandoc`

Then to convert to "github flavored markdown (gfm)" saving all figures in a folder called "media" in the current directory.

```
pandoc --to gfm --extract-media='.' week01WS01.docx -o week01S01.md
```

The result:  [week01S01.md](week01WS01.md)


Issues

1) figures need to be included with `<img>` tags and sized correctly.
2) Tables unlikely to render correctly
3) superscripts and subscripts need editing (I have a regular expression filter for that)

## pptx

### Step 1: extract the images to a folder named media

```
conda env create -f convert_env.yml
conda activate convert
python extact_images.py week01_C1_Introduction2018.pptx media
```

### Step 2: convert any wmf files to png using snaggit

### Step 3: make the markdown file

`python build_notebook.py week01_C1_Introduction2018.pptx media`

### Step 4: tweek in jupyter, resizing img tags as needed

### Step 5: convert to a slideshow using [rise](https://rise.readthedocs.io/en/stable/)



