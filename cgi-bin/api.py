import sys
import cgi
import xml.etree.ElementTree as ET

# constants

XML_HEADER = 'Content-type: application/xml \r\n\r\n'

# functions

def resp(msg):
  sys.stdout.write(msg)


# data

fields = cgi.FieldStorage()
resource = fields['resource'].value

# response

x_amltpv_response = ET.Element('amltpv-response')
x_resource = ET.SubElement(x_amltpv_response, 'resource')
x_resource.text = resource

# respond

resp(XML_HEADER)
resp(ET.tostring(x_amltpv_response))