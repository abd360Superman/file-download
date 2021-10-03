print("HTTP/1.0 200 OK\n")

import os

files = [{
    "name": "hello_world.txt",
    "blob": "Hello Wolrd!"
},
{
    "name": "hello_world.py",
    "blob": "print('Hello, World!')"
}]

css = """
body {
    background-color: black;
    color: white;
    font-family: 'Slabo 27px', serif;
}
.files {
    width: 100%;
}
"""
html = """
<html>
    <head>
        <title>File Storage - Macrofirm</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.2/css/bootstrap.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.2/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Slabo+27px&display=swap" rel="stylesheet">
        <style>
            %s
        </style>
    </head>
    <body>
"""
for i in range(len(files)):
    file = open(os.path.join('cgi-bin', files[i]['name']), 'wb+')
    file.write(bytes(files[i]['blob'], 'utf-8'))
    file.close()
    html += """
        <form enctype = "multipart/form-data" action = "download_file.py" method = "get" class='file'>
            <h3>%s</h3>
            <h4>File name: %s</h4>
            <input type='hidden' value=%s name='fname'>
            <h3 class='btn btn-info'><a href="%s" download>Download File</a></h3>
        </form>
    """ % (str(i+1), str(files[i]['name']), str(files[i]['name']), str(files[i]['name']))

html += "</body></html>"
print(html)