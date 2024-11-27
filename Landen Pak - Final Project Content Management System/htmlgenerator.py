import json

def generateHTML(title, content):
    with open ('index.html', 'w') as file:
        file.write(f'''
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>{title}</title>
                    </head>
                    <body>
                        <h1>{title}</h1>
                        <p>{content}</p>
                    </body>
                    </html>
                    ''')
