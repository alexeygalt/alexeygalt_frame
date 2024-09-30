from alexgalt_framework.api import API
from alexgalt_framework.middleware import SimpleCustomMiddleware, TimeMiddleware

app = API()


def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_exception_handler(custom_exception_handler)
app.add_middleware(SimpleCustomMiddleware)
app.add_middleware(TimeMiddleware)


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"


@app.route("/book")
class BooksResource:
    def get(self, request, resp):
        resp.text = "Books Page"

    def post(self, request, resp):
        resp.text = "Endpoint to create a book"


def handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler)


@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template("index.html", context={"name": "Bumbo", "title": "Best Framework"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}


@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text"


@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")
