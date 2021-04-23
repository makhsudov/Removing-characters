import re # Library for removing unnecessary symbols 

textArray = '''Lorem ips*um d№olor sit !amet,!!! con/sectetur adipisci/ng/ el«it, 
s«ed do eiusm[od tempor incidid#unt ut labore et dolore (magna ali$qua. 
Ut e@nim ad"m>inim v<<eniam, qui#s no^str&ud e*x!ercitation ul*lamco la#@boris nis-=-=-i ut 
a.liqui.p e.x ea c.mmodo con,,s.equat. '''

# Removing unnecessary characters 
textArray = re.sub(r"[\.\,\-\'=&$«»<()/!:*?>|№^#%@\[\]\"\"]", "", textArray )

# Removing spaces 
# textArray  = ''.join(textArray.split())
