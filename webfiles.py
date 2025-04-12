import os

depends = ["clear.py", "test.py", "ulib/fancy.py", "ulib/display.py"]

def program_page(uname):
    """ This function creates the html code for a website which lets the user select a program from the 
    user subdirectory and allows starting, stopping, deleting, or uploading a program using HTML forms. """
    # Get the list of Python files in the user subdirectory
    user_subdirectory = "./user/" + uname
    os.makedirs(user_subdirectory, exist_ok=True)
    # Copy the "test.py" file to the user subdirectory
    for filename in depends:
        source_file = "./user/"+filename
        destination_file = os.path.join(user_subdirectory, filename)
        if os.path.exists(source_file) and not os.path.exists(destination_file):
            with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
                dst.write(src.read())
    python_files = [f for f in os.listdir(user_subdirectory) if f.endswith('.py')]

    # Create the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Program Control</title>
    </head>
    <body>
        <h1>Program Control</h1>
        <form action="/programs" method="post">
            <label for="programSelect">Select a program:</label>
            <select id="programSelect" name="program">
    """

    # Add options for each Python file
    for file in python_files:
        html_content += f'<option value="{file}">{file}</option>\n'

    # Close the select element and add buttons
    html_content += """
            </select><br><br>
            <input type="hidden" name="uname" value="{uname}">
            <button type="submit" name="action" value="start">Start Program</button>
            <button type="submit" name="action" value="stop">Stop Program</button>
            <button type="submit" name="action" value="delete">Delete Program</button>
            <button type="submit" name="action" value="download">Download Program</button>
        </form>
        <br><br>
        <form action="/programs" method="post" enctype="multipart/form-data">
            <input type="hidden" name="uname" value="{uname}">
            <label for="fileUpload">Upload a program:</label>
            <input type="file" id="fileUpload" name="file" accept=".py">
            <button type="submit" name="action" value="upload">Upload</button>
            <button type="submit" name="action" value="lib_upload">Upload as library</button>
        </form>
    </body>
    </html>
    """.format(uname=uname)

    return html_content

def login_page():
    """ This function creates the html code for a website which lets the user enter a password. """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <script>
            function setUsername() {
                const username = document.getElementById('uname').value;
                document.cookie = "username=" + encodeURIComponent(username) + "; path=/";
            }
        </script>
    </head>
    <body>
        <h1>Enter Username</h1>
        <form action="/programs" method="post" onsubmit="setUsername()">
            <input type="text" id="uname" name="uname" required>
            <button type="submit">Enter</button>
        </form>
    </body>
    </html>
    """
    return html_content