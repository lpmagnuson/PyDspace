#!/usr/bin/env python

import csv
from pymarc import MARCReader
from os import listdir
from re import search

# change this line to match your folder structure
SRC_DIR = 'marc/'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('output/theses.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

csv_out.writerow(['id','collection','dc.contributor.advisor','dc.contributor.author','dc.contributor.committeeMember','dc.contributor.department','dc.date.copyright','dc.dateissued','dc.description','dc.description.abstract','dc.description.degree','dc.description.statementofresponsibility','dc.format.extent','dc.language.iso','dc.publisher','dc.rights.license','dc.rights.uri','dc.subject','dc.subject.other','dc.title','dc.type'])
     
for item in file_list:
  fd = file(SRC_DIR + '/' + item, 'r')
  reader = MARCReader(fd)
  for record in reader:
    dsid = collection = dccontributoradvisor = dccontributorauthor = dccontributorcommitteeMember = dccontributordepartment = dcdatecopyright = dcdateissued = dcdescription = dcdescriptionabstract = dcdescriptiondegree = dcdescriptionstatementofresponsibility = dcformatextent = dclanguageiso = dcpublisher = dcrights = dcrightslicense = dcrightsuri = dcsubject = dcsubjectother = dctitle = dctype = ''

     # online_identifier
    dsid = ('+')
    
    # collection
    collection = ('')
    
    # dc.contributor.advisor
    dccontributoradvisor = ''
    
    # dc.contributor.author
    if record['100'] is not None:
      dccontributorauthor = record['100']['a'].rsplit('.', 1)[0]
    elif record['110'] is not None:
      dccontributorauthor = record['110']['a'].rsplit('.', 1)[0]
    elif record['700'] is not None:
      dccontributorauthor = record['700']['a'].rsplit('.', 1)[0]
    elif record['710'] is not None:
      dccontributorauthor = record['710']['a'].rsplit('.', 1)[0]
      
    # dc.contributor.committeeMember
    dccontributorcommitteeMember = ''
      
    # dc.contributor.department
    if record ['690']['x'] is not None:
      dccontributordepartment = ('California State University, Northridge.  Department of ') + record['690']['x'].rsplit('.', 1)[0]
    
    # dc.date.copyright
    if record ['260']['c'] is not None:
      dcdatecopyright = record['260']['c'].rsplit('.', 1)[0]
       
    # dc.date.issued
    dcdateissued = ''
      
    # dc.description
    if record ['504'] is not None:
      dcdescription = record['504']['a'].rsplit('.', 1)[0]
    
    # dc.description.abstract
    dcdescriptionabstract = ''
    
    # dc.description.degree
    if record['502'] is not None:
      dcdescriptiondegree = record['502']['a'][record['502']['a'].find("(")+1:record['502']['a'].find(")")]
    
    # dc.description.statementofresponsibility
    if record ['245']['c'] is not None:
      dcdescriptionstatementofresponsibility = record['245']['c'].rsplit('.', 1)[0]
    
    #= dc.format.extent 
    dcformatextent = ''
     
    #dc.language.iso 
    dclanguageiso = ('en_US')
    
    #dc.publisher
    if record['260'] is not None:
      dcpublisher = record['260']['b']
    
    # dc.rights.license
    dcrightslicense = ('By signing and submitting this license, you the author grant permission to California State University, Northridge Graduate Studies to submit your thesis or dissertation, and any additional associated files you provide, to CSUN Scholarworks, the institutional repository of the California State University, Northridge, on your behalf.You grant to CSUN Scholarworks the non-exclusive right to reproduce and/or distribute your submission worldwide in electronic or any medium for non-commercial, academic purposes.  You agree that CSUN Scholarworks may, without changing the content, translate the submission to any medium or format, as well as keep more than one copy, for the purposes of security, backup and preservation.  You represent that the submission is your original work, and that you have the right to grant the rights contained in this license.  You also represent that your submission does not, to the best of your knowledge, infringe upon anyone\'s copyright.  If the submission contains material for which you do not hold copyright, or for which the intended use is not permitted, or which does not reasonably fall under the guidelines of fair use, you represent that you have obtained the unrestricted permission of the copyright owner to grant CSUN Scholarworks the rights required by this license, and that such third-party owned material is clearly identified and acknowledged within the text or content of the submission.  If the submission is based upon work that has been sponsored or supported by an agency or organization other than the California State University, Northridge, you represent that you have fulfilled any right of review or other obligations required by such contract or agreement.  CSUN Scholarworks will clearly identify your name(s) as the author(s) or owner(s) of the submission, and will not make any alterations, other than those allowed by this license, to your submission.')
    
    #dc.rights.uri
    dcrightsuri = ('http://scholarworks.csun.edu//handle/10211.2/286')
    
    #dc.subject  
    dcsubject = ''
    
    #dc.subject.other
    if record['690'] is not None:
      dcsubjectother = record['690']['a'] + " -- " + record['690']['z'] + " -- " + record['690']['x']
      
    # dc.title
    if record['245']['b'] is not None:
      dctitle = record['245']['a'] + " " + record['245']['b']
    if record['245']['a'] is not None:
      dctitle = record['245']['a'].rsplit('/', 1)[0]

    # dc.type
    dctype = ('Thesis')
       
    csv_out.writerow([dsid, collection, dccontributoradvisor, dccontributorauthor, dccontributorcommitteeMember, dccontributordepartment, dcdatecopyright, dcdateissued, dcdescription, dcdescriptionabstract, dcdescriptiondegree, dcdescriptionstatementofresponsibility, dcformatextent, dclanguageiso, dcpublisher, dcrightslicense, dcrightsuri, dcsubject, dcsubjectother, dctitle, dctype])
  fd.close()