# Manga to pdf
**UNIX ONLY**

Must have converter for e-books users. 
Just put manga.py file in folder, where you hold zip archives with manga and run it. 

Script will automaticly unzip archives, merge images into a single pdf file. One pdf for each zip. 

## What needed to run
Firs of all- zip archive with manga images and script. Marked by star (*). 

Install `imagemagick` via packet manager. 

Output file marked by sharp  

```
├── *manga.zip
├── manga
│   ├── 0000.jpeg
│   └── 0038.png
├── #manga.pdf
└── *manga.py
```