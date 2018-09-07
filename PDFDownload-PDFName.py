import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import os
import six

downloadPdfURL =input("Enter URL:")
page = urllib.request.urlopen(downloadPdfURL)
soup = BeautifulSoup(page, 'html.parser')

#function to save the pdf in folder. It will saved to folder where script runs.
def pdfDownload(url_pdf,pdf_name):
    response=requests.get(url_pdf)
    expdf=response.content
    egpdf=open(pdf_name,'wb')
    egpdf.write(expdf)
    egpdf.close()


for data in soup.find_all('body'):
    for aLink in soup.find_all('a'):
      getPdfLink = (aLink.get('href')) #This is the pdf link in href. And assumes that its in format http://somewwebsite.com/downloads/name.pdf
      #In some cases only relative URL is added on the href link like "/downloads/name.pdf"
      #In those cases please uncomment below code and add domainName
      #domainName = "https://somedomainname.com"
      #getPdfLink = domainName+getPdfLink
      
     
      
     #Get the Full Path of PDF
      fullPathOfPDF = urlparse(getPdfLink) 
     #Gets the file name
      pdf_name = os.path.basename(fullPathOfPDF.path)
      
      if isinstance(pdf_name, six.string_types):
        if( pdf_name.find("pdf")>0):
         print(getPdfLink)
         pdfDownload(getPdfLink,pdf_name)
        
        
        
       
