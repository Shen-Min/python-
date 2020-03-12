def aplication(file_path):

    if file_path == "/index.html":
        response_body = "hello web!".encode('utf-8')

    elif file_path == "/login.html":

        with open("./post.html", 'rb') as f:
            content = f.read()
        response_body = content

    elif file_path.endswith(".jpg"):
        with open("." + file_path, 'rb') as f:
            content = f.read()
        response_body = content
    else:
        response_body = "no page is shown!".encode("utf-8")

    return response_body
