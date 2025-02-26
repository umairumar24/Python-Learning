letter = ''' Dear <|Name|>,
             You are selected!
             <|Date|>'''

print(letter.replace("<|Name|>", "Umair").replace("<|Date|>", "15-Febuary-2025"))