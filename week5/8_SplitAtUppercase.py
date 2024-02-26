import re

#text = "TodayIPassedLinalgMidterm"
#print(re.findall('[A-Z][^A-Z]*', text))
ini_str = 'TodayIPassedLinAlgMidterm'

res_list = re.findall('[A-Z][^A-Z]*', ini_str)

print("Resultant prefix", str(res_list))