from archer_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', header_menu=request.get('header_menu'), title='Main', my_url=request.get('url'))

class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', header_menu=request.get('header_menu'), title='Page', my_url=request.get('url'))

class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', header_menu=request.get('header_menu'), title='Contact', my_url=request.get('url'))

class Examples:
    def __call__(self, request):
        return '200 OK', render('examples.html', header_menu=request.get('header_menu'), title='Examples', my_url=request.get('url'))

class Another_page:
    def __call__(self, request):
        return (
            '200 OK',
            render('another_page.html', header_menu=request.get('header_menu'), title='Another page', my_url=request.get('url'))
        )
