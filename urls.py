from datetime import date
from views import Index, Page, Contact, Examples, Another_page


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['header_menu'] = [
        {'name': "Home", 'link': "/", 'selected': False},
        {'name': "Examples", 'link': "/examples/", 'selected': False},
        {'name': "A page", 'link': "/page/", 'selected': False},
        {'name': "Another page", 'link': "/another_page/", 'selected': False},
        {'name': "Contact us", 'link': "/contact/", 'selected': False},
    ]


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page/': Page(),
    '/examples/': Examples(),
    '/contact/': Contact(),
    '/another_page/': Another_page(),
}
