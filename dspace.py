#!/usr/bin/env python

import csv
from pymarc import MARCReader
from os import listdir
from re import search

# change this line to match your folder structure
SRC_DIR = 'marc/'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('printjournals.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

csv_out.writerow(['id','collection','dc.contributor.advisor','dc.contributor.author','dc.contributor.committeeMember','dc.contributor.department','dc.date.copyright','dc.date.issued','dc.description','dc.description.abstract','dc.description.degree','dc.description.statementofresponsibility','dc.format.extent','dc.language.iso','dc.publisher','dc.rights','dc.rights.license','dc.rights.uri','dc.subject','dc.subject.other','dc.title','dc.type'])
     
for item in file_list:
  fd = file(SRC_DIR + '/' + item, 'r')
  reader = MARCReader(fd)
  for record in reader:
    id = collection = dc.contributor.advisor = dc.contributor.author = dc.contributor.committeeMember = dc.contributor.department = dc.date.copyright = dc.date.issued = dc.description = dc.description.abstract = dc.description.degree = dc.description.statementofresponsibility = dc.format.extent = dc.language.iso = dc.publisher = dc.rights = dc.rights.license = dc.rights.uri = dc.subject = dc.subject.other = dc.title = dc.type = ''

     # online_identifier
    id = ('+')
    
    # collection
    collection = ('10211.2/286')
    
    # dc.contributor.advisor
    dc.contributor.advisor = ''
    
    # dc.contributor.author
    if record['100'] is not None:
      first_author = record['100']['a']
    elif record['110'] is not None:
      first_author = record['110']['a']
    elif record['700'] is not None:
      first_author = record['700']['a']
    elif record['710'] is not None:
      first_author = record['710']['a']
      
    # dc.contributor.committeeMember
    dc.contributor.committeeMember = ''
      
    # dc.contributor.department
    if record ['690']['x'] is not None:
      dc.contributor.department = ('California State University, Northridge.  Department of ') + record['863']['i']
    
    # dc.date.copyright
    if record ['260']['c'] is not None:
      dc.date.copyright = record['260']['c']
       
    # dc.date.issued
    if record ['260']['c'] is not None:
      dc.date.copyright = record['260']['c']
      
    # dc.description
    if record ['504'] is not None:
      dc.description = record['504']
    
    # dc.description.abstract
    dc.description.abstract = ''
    
    # dc.description.degree
    if record ['502']['a'] is not None:
      sep = '('
      dc.description.degree = record['502']['a'].split(sep, 3)[-1]
    
    # dc.description.statementofresponsibility
    if record ['245']['c'] is not None:
      dc.description.statementofresponsibility = record['245']['c']
    
    #= dc.format.extent 
    dc.format.extent = record['856']['u']
     
    #dc.language.iso 
    dc.language.iso = ('en_US')
    
    #dc.publisher
    if record['260'] is not None:
      dc.publisher = record['260']['b']
    
    # dc.rights 
    dc.rights = ('California State University, Northridge theses are protected by copyright. Access restricted to CSUN users only.')
    
    # dc.rights.license
    dc.rights.license = ('By signing and submitting this license, you the author grant permission to 
CSUN Graduate Studies to submit your thesis or dissertation, and any additional 
associated files you provide, to CSUN ScholarWorks, the institutional repository 
of the California State University, Northridge, on your behalf.


You grant to CSUN ScholarWorks the non-exclusive right to reproduce and/or 
distribute your submission worldwide in electronic or any medium for non-commercial, 
academic purposes.


You agree that CSUN ScholarWorks may, without changing the content, translate 
the submission to any medium or format, as well as keep more than one copy, 
for the purposes of security, backup and preservation.


You represent that the submission is your original work, and that you have the 
right to grant the rights contained in this license.  You also represent that 
your submission does not, to the best of your knowledge, infringe upon anyone\'s 
copyright.


If the submission contains material for which you do not hold copyright, or 
for which the intended use is not permitted, or which does not reasonably 
fall under the guidelines of fair use, you represent that you have obtained 
the unrestricted permission of the copyright owner to grant CSUN ScholarWorks 
the rights required by this license, and that such third-party owned material 
is clearly identified and acknowledged within the text or content of the 
submission.


If the submission is based upon work that has been sponsored or supported by an 
agency or organization other than the California State University, Northridge, 
you represent that you have fulfilled any right of review or other obligations 
required by such contract or agreement.


CSUN ScholarWorks will clearly identify your name(s) as the author(s) or owner(s) 
of the submission, and will not make any alterations, other than those allowed by 
this license, to your submission')
    
    #dc.rights.uri
    dc.rights.uri = ('http://scholarworks.csun.edu//handle/10211.2/286')
    
    #dc.subject  
    dc.subject = ''
    
    #dc.subject.other
    dc.subject.other = ''
      
    # dc.title
    if record['245'] is not None:
      dc.title = record['245']['a']
      if record['245']['b'] is not None:
        dc.title = dc.title + " " + record['245']['b']

	# dc.type
    dc.type = ('Thesis')
       
    csv_out.writerow([id, collection, dc.contributor.advisor, dc.contributor.author, dc.contributor.committeeMember, dc.contributor.department, dc.date.copyright, dc.date.issued, dc.description, dc.description.abstract, dc.description.degree, dc.description.statementofresponsibility, dc.format.extent, dc.language.iso, dc.publisher, dc.rights, dc.rights.license, dc.rights.uri, dc.subject, dc.subject.other, dc.title, dc.type])
  fd.close()