# converting docx, tex and pptx to markdown

## docx

`conda install pandoc`

Then to convert to "github flavored markdown (gfm)" saving all figures in a folder called "media" in the current directory.

```
pandoc --to gfm --extract-media='.' week01WS01.docx -o week01S01.md
```

The result:  [week01S01.md](week01S01.md)


Issues

1) figures need to be included with `<img>` tags and sized correctly.
2) Tables unlikely to render correctly
3) superscripts and subscripts need editing (I have a regular expression filter for that)

