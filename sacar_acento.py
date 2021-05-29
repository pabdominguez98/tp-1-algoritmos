import unidecode

string = 'máñaga ñacurutú ñeembucú'

string_s = string.replace('ñ', '@')

o_string = unidecode.unidecode(string_s)

string_n = o_string.replace('@', 'ñ')

print(string_n)