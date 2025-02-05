s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s1 = s.lstrip('{').rstrip('}').split('},{')
print(s1)