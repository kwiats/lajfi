from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notes

class NotesModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.note_data = {
            'title': 'Test Note',
            'content': 'This is a test note content.',
            'user': self.user,
            'status': 'draft'
        }

    def test_create_note_with_valid_data(self):
        note = Notes.objects.create(**self.note_data)
        self.assertIsNotNone(note.uuid)
        self.assertEqual(note.title, 'Test note')
        self.assertEqual(note.content, 'This is a test note content.')
        self.assertEqual(note.user, self.user)
        self.assertEqual(note.status, 'draft')
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    def test_create_note_without_title(self):
        self.note_data.pop('title')
        note = Notes.objects.create(**self.note_data)
        self.assertEqual(note.title, self.note_data['content'][:50].capitalize())
        self.assertEqual(note.content, 'This is a test note content.')
        self.assertEqual(note.user, self.user)
        self.assertEqual(note.status, 'draft')
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    def test_edit_note_with_valid_data(self):
        note = Notes.objects.create(**self.note_data)
        note.title = 'Edited Note'
        note.content = 'Edited content.'
        note.save()
        edited_note = Notes.objects.get(uuid=note.uuid)
        self.assertEqual(edited_note.title, 'Edited note')
        self.assertEqual(edited_note.content, 'Edited content.')
        self.assertGreater(edited_note.updated_at, edited_note.created_at)

    def test_get_existing_note_by_id(self):
        note = Notes.objects.create(**self.note_data)
        found_note = Notes.objects.get(uuid=note.uuid)
        self.assertEqual(found_note.title, 'Test note')
        self.assertEqual(found_note.content, 'This is a test note content.')

    def test_get_nonexistent_note_by_id(self):
        with self.assertRaises(Notes.DoesNotExist):
            Notes.objects.get(uuid=999)

    def test_get_all_notes(self):
        Notes.objects.create(**self.note_data)
        self.note_data['title'] = 'Test Note 2'
        Notes.objects.create(**self.note_data)
        notes = Notes.objects.all()
        self.assertEqual(len(notes), 2)

    def test_delete_existing_note_by_id(self):
        note = Notes.objects.create(**self.note_data)
        note_id = note.uuid
        note.delete()
        with self.assertRaises(Notes.DoesNotExist):
            Notes.objects.get(uuid=note_id)

    def test_delete_nonexistent_note_by_id(self):
        note_count_before = Notes.objects.count()
        Notes.objects.filter(uuid=999).delete()
        note_count_after = Notes.objects.count()
        self.assertEqual(note_count_before, note_count_after)

    def test_filter_notes_by_title(self):
        Notes.objects.create(**self.note_data)
        self.note_data['title'] = 'Special Note'
        Notes.objects.create(**self.note_data)
        filtered_notes = Notes.objects.filter(title__icontains='Special')
        self.assertEqual(len(filtered_notes), 1)
        self.assertEqual(filtered_notes[0].title, 'Special note')

    def test_mass_create_edit_delete_notes(self):
        notes = [Notes(title=f'Note {i}', content=f'Content {i}', user=self.user, status='draft') for i in range(1, 101)]
        Notes.objects.bulk_create(notes)

        all_notes = Notes.objects.all()
        self.assertEqual(len(all_notes), 100)

        for note in all_notes:
            note.title = f'Edited {note.title}'
        Notes.objects.bulk_update(all_notes, ['title'])

        edited_notes = Notes.objects.all()
        for note in edited_notes:
            self.assertTrue(note.title.startswith('Edited'))

        Notes.objects.filter(uuid__in=[note.uuid for note in edited_notes[:50]]).delete()

        remaining_notes = Notes.objects.all()
        self.assertEqual(len(remaining_notes), 50)
