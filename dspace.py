#!/usr/bin/env python

import csv
from pymarc import MARCReader
from os import listdir
from re import search

# change this line to match your folder structure
SRC_DIR = 'marc/'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('output/theses.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

csv_out.writerow(['id','collection','dc.contributor.advisor','dc.contributor.author','dc.contributor.committeeMember','dc.contributor.department','dc.date.copyright','dc.dateissued','dc.description','dc.description.abstract','dc.description.degree','dc.description.statementofresponsibility','dc.format.extent','dc.language.iso','dc.publisher','dc.rights','dc.rights.license','dc.rights.uri','dc.subject','dc.subject.other','dc.title','dc.type'])
     
for item in file_list:
  fd = file(SRC_DIR + '/' + item, 'r')
  reader = MARCReader(fd)
  for record in reader:
    id = collection = dccontributoradvisor = dccontributorauthor = dccontributorcommitteeMember = dccontributordepartment = dcdatecopyright = dcdateissued = dcdescription = dcdescriptionabstract = dcdescriptiondegree = dcdescriptionstatementofresponsibility = dcformatextent = dclanguageiso = dcpublisher = dcrights = dcrightslicense = dcrightsuri = dcsubject = dcsubjectother = dctitle = dctype = ''

     # online_identifier
    id = ('+')
    
    # collection
    collection = ('10211.2/286')
    
    # dc.contributor.advisor
    dccontributoradvisor = ''
    
    # dc.contributor.author
    if record['100'] is not None:
      dccontributorauthor = record['100']['a']
    elif record['110'] is not None:
      dccontributorauthor = record['110']['a']
    elif record['700'] is not None:
      dccontributorauthor = record['700']['a']
    elif record['710'] is not None:
      dccontributorauthor = record['710']['a']
      
    # dc.contributor.committeeMember
    dccontributorcommitteeMember = ''
      
    # dc.contributor.department
    if record ['690']['x'] is not None:
      dccontributordepartment = ('California State University, Northridge.  Department of ') + record['690']['x']
    
    # dc.date.copyright
    if record ['260']['c'] is not None:
      dcdatecopyright = record['260']['c']
       
    # dc.date.issued
    if record ['260']['c'] is not None:
      dcdatecopyright = record['260']['c']
      
    # dc.description
    if record ['504'] is not None:
      dcdescription = record['504']['a']
    
    # dc.description.abstract
    dcdescriptionabstract = ''
    
    # dc.description.degree
    if record['502'] is not None:
      dcdescriptiondegree = record['502']['a'][record['502']['a'].find("(")+1:record['502']['a'].find(")")]
    
	#record ['502']['a'] is not None:
      #sep = '('
      #dcdescriptiondegree = record['502']['a'].split(sep, 3)[-1]
    
    # dc.description.statementofresponsibility
    if record ['245']['c'] is not None:
      dcdescriptionstatementofresponsibility = record['245']['c']
    
    #= dc.format.extent 
    dcformatextent = ''
     
    #dc.language.iso 
    dclanguageiso = ('en_US')
    
    #dc.publisher
    if record['260'] is not None:
      dcpublisher = record['260']['b']
    
    # dc.rights 
    dcrights = ('California State University, Northridge theses are protected by copyright. Access restricted to CSUN users only.')
    
    # dc.rights.license
    dcrightslicense = ('')
    
    #dc.rights.uri
    dcrightsuri = ('http://scholarworks.csun.edu//handle/10211.2/286')
    
    #dc.subject  
    dcsubject = ''
    
    #dc.subject.other
    dcsubjectother = ''
      
    # dc.title
    if record['245'] is not None:
      dctitle = record['245']['a']
      if record['245']['b'] is not None:
        dctitle = dctitle + " " + record['245']['b']

    # dc.type
    dctype = ('Thesis')
       
    csv_out.writerow([id, collection, dccontributoradvisor, dccontributorauthor, dccontributorcommitteeMember, dccontributordepartment, dcdatecopyright, dcdateissued, dcdescription, dcdescriptionabstract, dcdescriptiondegree, dcdescriptionstatementofresponsibility, dcformatextent, dclanguageiso, dcpublisher, dcrights, dcrightslicense, dcrightsuri, dcsubject, dcsubjectother, dctitle, dctype])
  fd.close()