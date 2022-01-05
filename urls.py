from datetime import date
from views import Index, Page, Contact, Examples, Another_page


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page/': Page(),
    '/examples/': Examples(),
    '/contact/': Contact(),
    '/another_page/': Another_page(),
}
