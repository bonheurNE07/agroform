import re 

dd = ["1 1983 8 0173159086 ~","1 2001 7 0036527 0 9","@3 2022 5 1234567890 32","4 1999 2 9876543 6 54","5 2005 4 2345678901 89"]
for dd in dd:
    national_no_re = re.compile(r"\d{1} *\d{4} *\d{1} *\d{7} *\d{1} *\d{2}")
    national_no = re.search(national_no_re, dd)
    if national_no:
        ID = dd[national_no.start():national_no.end()]
        print(ID)