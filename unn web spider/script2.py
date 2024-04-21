# Script to extract JAMB numbers from pdf and save them in an arraay

from pdfminer.high_level import extract_pages, extract_text
import re
import sys 

text_body = extract_text("admission_list.pdf")
#print(text_body)


# JAMB regnumber regex
jamb_numbers = []
jamb_number_pattern = re.compile(r'^(?:[2][0-9]{3})(?:[0-9]{7}[A-Z]{3}|[0-9]{5}[A-Z]{5})$')

jamb_number = jamb_number_pattern.findall()
jamb_numbers.append(jamb_number)
print(jamb_numbers)

