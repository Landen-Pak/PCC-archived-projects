import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1234

server.bind((host, port))

# exit on stopping script
while True:
    print(f'Listening...')

    server.listen(1)

    clnt, addr = server.accept()
    clnt.recv(1024)

    with open('index.html', 'r') as file: # get contents of html file
        html_content = file.read()

    # make http reponse (I had to look this up)
    response = f"""\
    HTTP/1.1 200 OK

    {html_content}"""

    clnt.send(response.encode('utf-8')) # send response

    print(f'Successfully sent html file to {addr}\n\n')
