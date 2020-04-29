import PyPDF2
import os
import re
import sys

# function that scrapes every info off a pdf file
def scrape(file):
    phone, mail, linkedin, github = "none", "none", "none", "none"
    
    report.write(file)
    report.write("\n\nSkills:\n")

    # open pdf file
    pdfFile = open(file, 'rb')
    reader = PyPDF2.PdfFileReader(pdfFile,strict=False)

    # check every page
    for p in range(reader.numPages):
        page = reader.getPage(p)
        text = page.extractText()

        if phoneRe.findall(text):
            phone = phoneRe.findall(text)[0]

        if mailRe.findall(text):
            mail = mailRe.findall(text)[0]

        if linkedinRe.findall(text):
            linkedin = linkedinRe.findall(text)[0]

        if githubRe.findall(text):
            github = githubRe.findall(text)[0]

        # go and check input in the argument list
        for i in range(len(sys.argv)):
            if i==0:
                pass
            else:
                skill = sys.argv[i]
                regex = r'\b' + re.escape(skill) + r'.?\b'
                if re.compile(regex, re.I).search(text):
                    report.write(skill)
                    report.write('\n')

    report.write('\nphone: ')
    report.write(phone)
    report.write('\nmail: ')
    report.write(mail)
    report.write('\nlinkedin: ')
    report.write(linkedin)
    report.write('\ngithub: ')
    report.write(github)

    report.write('\n\n')
    report.write('-'*30)
    report.write('\n\n')
# end of scrape function


# here are the various regexes used in this application
mailRe = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.I)
phoneRe = re.compile(r'[\d]{3,}\s[\d]{3,}')
githubRe = re.compile(r'[github.com]+.*\b', re.I)
linkedinRe = re.compile(r'[w\.]+[linkedin].*\b', re.I)
pdfRe = re.compile(r'.*[.pdf]$', re.I) 

pdfs = [] # list storing cvs names

# folder containing the cvs
os.chdir(r'C:\Users\feder\Desktop\Coding\Curriculum')

# find every pdf file in the folder and append it to a list
for file in os.listdir():
    if pdfRe.findall(file):
        pdfs.append(pdfRe.findall(file)[0])

report = open(r'report.txt', 'a') 

# iterate trough them
for pdf in pdfs:
    scrape(pdf)

report.close()
