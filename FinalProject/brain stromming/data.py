cl =[{"hello":"world","status":"active","age":52},{"hello":"world","status":"active","age":52}]
#txt = str(cl)

txt = f'{cl}'
print(txt)
print(type(txt))

txt.replace("hello",'namaste')
print(txt)