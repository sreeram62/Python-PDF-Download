# Python-PDF-Download
To download all PDF's from a given web page using python Script

The script assumes first finds all the anchor tags ("a") and then takes the href from the a tags. 

Then it finds if the href has .pdf at the end. If so a function runs to download the PDF.

The whole script assumes that the pdf link is in format http://somewebsite.com/downloads/name.pdf

**In few cases relative path is used in that case the script fails. Ex path is "downloads/name.pdf" in that case please uncomment few lines of code which helps to get Full URL and update the domain name in variable "domainName**

Lines to be uncommented in case relative URL is used:

     #domainName = "https://somedomainname.com" 
  
     #getPdfLink = domainName+getPdfLink <br/>
  
     And make sure domainName variable is updated.
