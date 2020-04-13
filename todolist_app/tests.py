from django.test import TestCase, Client


class TestTodoList(TestCase):

    def test_login(self):
        c = Client()
        response = c.post('/login', {
            'username': 'aramis', 'password': 'agustin20'
            })
        self.assertEquals(response.status_code, 200)
         
