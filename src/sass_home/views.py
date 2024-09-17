# import pathlib
from django.shortcuts import render
from django.http import HttpResponse

# this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # print(this_dir)
    title = {
        "name" : "Uchechukwu"
    }
    html_ = """
    <!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <h1>This is just a {name} test</h1>
    </body>

</html>
    """.format(**title)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)