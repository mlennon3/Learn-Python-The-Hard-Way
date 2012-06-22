import web

urls = (
    '/(.*)', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self, name):
        greeting = "Hello, World"
        return render.index(greeting, name)

if __name__ == "__main__":
    app.run()
