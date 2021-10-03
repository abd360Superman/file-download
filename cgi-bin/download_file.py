import cgi
form = cgi.FieldStorage()

filename = form['fname'].value

print('Content-Type:application/octet-stream; name="%s"' % filename)
print('Content-Disposition: attachment; filename="%s"' % filename)
print("")

with open(filename, 'rb') as fo:
    print(open(filename).read())
    fo.close()