import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("scrapper testpdf2.pdf")
#print(text)


email_pattern = re.compile(r'[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*')
phone_number_pattern = re.compile(r"^(?:\+234|0)?[789][0-9]{10}$")
phone_number = phone_number_pattern.findall(text)
email = email_pattern.findall(text)

print(email,phone_number)
