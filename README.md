## Curriculum Scraper
I recently completed the brilliant [Automate The Boring Stuff](https://www.udemy.com/course/automate/) course and I wrote this little Python script to apply what I learned in a useful project. <br>
This program is designed to extract useful informations from curriculums in order to save time while going trough numerous applications. 
The script opens every pdf file in a folder and creates a report.txt file with relevant skills and contact informations for every CV. <br>
You can specify which skills you are looking for in a candidate by writing them in the command line, for example:
```
python curriculum_scraper.py Java C++ Photoshop AWS
```
Will write a report confirming if Java, C++, Photoshop, and AWS skills are mentioned in the CV. <br>
To run this script you will need Python and the latest version PyPDF2, you can install it with the command `pip install PyPDF2`

### The Report File
When the program is run successfully the report.txt file is created in the same folder analyzed, the file collects the name of the pdf, all the skills specified in the command line contact details such as phone number, mail, Linkedin and Github profiles.
A little example, analyzing a folder with two versions of my curriculum, using this command:
```
python curriculum_scraper.py Java C++ HTML CSS Python
```
returned this result
```
Curriculum Federico Mannucci.pdf

Skills:
HTML
CSS
Python

phone: 324 679072
mail: federicomannucci@gmail.com
linkedin: www.linkedin.com/in/fmabss
github: https://github.com/Federico-abss

------------------------------

CV Federico Mannucci.pdf

Skills:
C++
HTML
CSS
Python

phone: 324 679072
mail: federicomannucci@gmail.com
linkedin: www.linkedin.com/in/fmabss
github: https://github.com/Federico-abss

------------------------------
```
As a little disclaimer, this program utilizes regular expressions to extract the informations from the files, the ones I used are very basic and might not be able to catch every format of phone number or website.

### Certificate
![ATBS Certificate](Automate%20The%20Boring%20Stuff.jpg)
