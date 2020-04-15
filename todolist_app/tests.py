from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Priority, Todo


class TestTodoList(TestCase):

    def test_todo_list_login(self):
        client = Client()
        user = User.objects.create(username='aramis')
        user.set_password('agustin20')
        user.save()
        response = client.post('/login', {
            'username': 'aramis', 'password': 'agustin20'
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_todo_list_invalid_login(self):
        client = Client()
        user = User.objects.create(username='aramis')
        user.set_password('agustin20')
        user.save()
        response = client.post(
            '/login',
            {
                'username': 'aramis',
                'password': 'passwordinvalid'
            },
            follow=True,
        )
        self.assertEquals(response.status_code, 200)

    def test_todo_list_incorrect_login(self):
        c = Client()
        result = c.login(
            username='aramis',
            password='invalidPassword'
        )
        self.assertFalse(result)

    def test_todo_list_user_logged(self):
        c = Client()
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c.login(username='testuser', password='12345')
        response = c.get('')
        self.assertEqual(response.status_code, 200)


class TestTodoCreate(TestCase):

    def setUp(self):
        self.priority = Priority.objects.create(name='Low', order=1)
        self.client = Client()
        self.user = User.objects.create(username='aramis')
        self.user.set_password('agustin20')
        self.user.save()

    def test_create_todo_status_code(self):
        self.client.force_login(self.user)
        response = self.client.post('/new/', {
            'tittle': 'Taskk 1',
            'description': 'Task 2',
            'done': False,
            'priority': self.priority.id
        })
        self.assertEquals(response.status_code, 302)

    def test_create_todo(self):
        # Otra forma de hacer login
        self.client.force_login(self.user)

        # self.client.login(
        #     username='aramis',
        #     password='agustin20'
        #     )
        response = self.client.post('/new/', {
            'tittle': 'Taskk 1',
            'description': 'Task 2',
            'done': False,
            'priority': self.priority.id
        }, follow=True)
        id = response.context['object'].id
        self.assertRedirects(response, '/view/'+str(id))
        self.assertEquals(response.status_code, 200)

    def test_failed_create_todo(self):
        self.client.force_login(self.user)
        response = self.client.post('/new/', {
            'tittle': 'Taskk 1',
            'description': '',
            'done': False,
            'priority': self.priority.id
        })
        self.assertEquals(response.status_code, 200)


class TestTodoDelete(TestCase):

    def test_delete_todo(self):
        pass


class TestTodoView(TestCase):

    def setUp(self):
        todo = Todo.objects.create(
            tittle='task1',
            description='Descripcion de tarea 1',
            assigned_user=self.user,
            done=False,
            created='2020-04-10',
            updated='2020-04-10',
            created_by=self.user,
            updated_by=self.user,
            priority=self.priority,
        )
