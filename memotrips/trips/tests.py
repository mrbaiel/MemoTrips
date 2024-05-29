from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm


class TripsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_login_view_authenticated(self):
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('index'))

    def test_login_view_post_valid_credentials(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'testpassword'}
        )
        self.assertRedirects(response, reverse('index'))

    def test_login_view_post_invalid_credentials(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'wrongpassword'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Invalid username or password')

    def test_logout_view_authenticated(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_logout_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_index_view_authenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('login'))

    def test_welcome_view_authenticated(self):
        response = self.client.get(reverse('welcome'))
        self.assertRedirects(response, reverse('index'))

    def test_welcome_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')

    def test_add_note_view_get(self):
        response = self.client.get(reverse('add_note'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_note.html')

    def test_add_note_view_post_valid_data(self):
        response = self.client.post(
            reverse('add_note'),
            {'title': 'Test Note', 'content': 'Test content'}
        )
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.first()
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'Test content')
        self.assertEqual(note.user, self.user)

    def test_add_note_view_post_invalid_data(self):
        response = self.client.post(
            reverse('add_note'),
            {'title': '', 'content': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_note.html')
        self.assertContains(response, 'This field is required.')

    def test_edit_note_view_get(self):
        note = Note.objects.create(
            title='Test Note',
            content='Test content',
            user=self.user
        )
        response = self.client.get(reverse('edit_note', args=[note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_note.html')

    def test_edit_note_view_post_valid_data(self):
        note = Note.objects.create(
            title='Test Note',
            content='Test content',
            user=self.user
        )
        response = self.client.post(
            reverse('edit_note', args=[note.pk]),
            {'title': 'Updated Note', 'content': 'Updated content'}
        )
        self.assertRedirects(response, reverse('index'))
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')
        self.assertEqual(note.content, 'Updated content')

    def test_edit_note_view_post_invalid_data(self):
        note = Note.objects.create(
            title='Test Note',
            content='Test content',
            user=self.user
        )
        response = self.client.post(
            reverse('edit_note', args=[note.pk]),
            {'title': '', 'content': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_note.html')
        self.assertContains(response, 'This field is required.')

    def test_delete_note_view_get(self):
        note = Note.objects.create(
            title='Test Note',
            content='Test content',
            user=self.user
        )
        response = self.client.get(reverse('delete_note', args=[note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete_note.html')

    def test_delete_note_view_post(self):
        note = Note.objects.create(
            title='Test Note',
            content='Test content',
            user=self.user
        )
        response = self.client.post(reverse('delete_note', args=[note.pk]))
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Note.objects.count(), 0)
