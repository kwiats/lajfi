from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from task.models import Task
from schedule.models import Event
from shopping.models import ShoppingItem, ShoppingList
from progress.models import Progress
from reminder.models import Reminder
from notes.models import Notes
from django.utils.timezone import now, timedelta

class Command(BaseCommand):
    help = 'Create sample data for users'

    def handle(self, *args, **kwargs):
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin.set_password('admin')
            admin.save()
            self.stdout.write(self.style.SUCCESS('Admin user created'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))

        for i in range(1, 6):
            user, created = User.objects.get_or_create(
                username=f'user{i}',
                defaults={
                    'email': f'user{i}@example.com',
                }
            )
            if created:
                user.set_password(f'user{i}password')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'User{i} created'))
            else:
                self.stdout.write(self.style.WARNING(f'User{i} already exists'))

            # Generate sample data for each user
            self.create_sample_data_for_user(user)

    def create_sample_data_for_user(self, user):
        # Create sample tasks
        tasks = [
            {'title': f'Task 1 for {user.username}', 'description': f'Description for task 1', 'priority': 1, 'due_date': now() + timedelta(days=1), 'user': user, 'completed': False},
            {'title': f'Task 2 for {user.username}', 'description': f'Description for task 2', 'priority': 2, 'due_date': now() + timedelta(days=2), 'user': user, 'completed': False},
            {'title': f'Task 3 for {user.username}', 'description': f'Description for task 3', 'priority': 3, 'due_date': now() + timedelta(days=3), 'user': user, 'completed': True},
            {'title': f'Task 4 for {user.username}', 'description': f'Description for task 4', 'priority': 1, 'due_date': now() + timedelta(days=4), 'user': user, 'completed': False},
            {'title': f'Task 5 for {user.username}', 'description': f'Description for task 5', 'priority': 2, 'due_date': now() + timedelta(days=5), 'user': user, 'completed': False},
            {'title': f'Task 6 for {user.username}', 'description': f'Description for task 6', 'priority': 3, 'due_date': now() + timedelta(days=6), 'user': user, 'completed': False},
            {'title': f'Task 7 for {user.username}', 'description': f'Description for task 7', 'priority': 1, 'due_date': now() + timedelta(days=7), 'user': user, 'completed': False},
            {'title': f'Task 8 for {user.username}', 'description': f'Description for task 8', 'priority': 2, 'due_date': now() + timedelta(days=8), 'user': user, 'completed': False},
            {'title': f'Task 9 for {user.username}', 'description': f'Description for task 9', 'priority': 3, 'due_date': now() + timedelta(days=9), 'user': user, 'completed': True},
            {'title': f'Task 10 for {user.username}', 'description': f'Description for task 10', 'priority': 1, 'due_date': now() + timedelta(days=10), 'user': user, 'completed': False},
        ]
        for task_data in tasks:
            task = Task.objects.create(**task_data)
            # Create progress for each task
            Progress.objects.create(task=task, progress=0)
            Progress.objects.create(task=task, progress=50)
            Progress.objects.create(task=task, progress=100)

        self.stdout.write(self.style.SUCCESS(f'Sample tasks and progress created for {user.username}'))

        # Create sample notes
        notes = [
            {'title': f'Note 1 for {user.username}', 'content': f'Content for note 1', 'user': user},
            {'title': f'Note 2 for {user.username}', 'content': f'Content for note 2', 'user': user},
            {'title': f'Note 3 for {user.username}', 'content': f'Content for note 3', 'user': user},
            {'title': f'Note 4 for {user.username}', 'content': f'Content for note 4', 'user': user},
            {'title': f'Note 5 for {user.username}', 'content': f'Content for note 5', 'user': user},
        ]
        for note_data in notes:
            Notes.objects.create(**note_data)

        self.stdout.write(self.style.SUCCESS(f'Sample notes created for {user.username}'))

        # Create sample events
        events = [
            {'title': f'Event 1 for {user.username}', 'description': f'Description for event 1', 'start_time': now() + timedelta(days=1), 'end_time': now() + timedelta(days=1, hours=2), 'user': user},
            {'title': f'Event 2 for {user.username}', 'description': f'Description for event 2', 'start_time': now() + timedelta(days=2), 'end_time': now() + timedelta(days=2, hours=2), 'user': user},
            {'title': f'Event 3 for {user.username}', 'description': f'Description for event 3', 'start_time': now() + timedelta(days=3), 'end_time': now() + timedelta(days=3, hours=2), 'user': user},
            {'title': f'Event 4 for {user.username}', 'description': f'Description for event 4', 'start_time': now() + timedelta(days=4), 'end_time': now() + timedelta(days=4, hours=2), 'user': user},
            {'title': f'Event 5 for {user.username}', 'description': f'Description for event 5', 'start_time': now() + timedelta(days=5), 'end_time': now() + timedelta(days=5, hours=2), 'user': user},
            {'title': f'Event 6 for {user.username}', 'description': f'Description for event 6', 'start_time': now() + timedelta(days=6), 'end_time': now() + timedelta(days=6, hours=2), 'user': user},
            {'title': f'Event 7 for {user.username}', 'description': f'Description for event 7', 'start_time': now() + timedelta(days=7), 'end_time': now() + timedelta(days=7, hours=2), 'user': user},
            {'title': f'Event 8 for {user.username}', 'description': f'Description for event 8', 'start_time': now() + timedelta(days=8), 'end_time': now() + timedelta(days=8, hours=2), 'user': user},
            {'title': f'Event 9 for {user.username}', 'description': f'Description for event 9', 'start_time': now() + timedelta(days=9), 'end_time': now() + timedelta(days=9, hours=2), 'user': user},
            {'title': f'Event 10 for {user.username}', 'description': f'Description for event 10', 'start_time': now() + timedelta(days=10), 'end_time': now() + timedelta(days=10, hours=2), 'user': user},
        ]
        for event_data in events:
            Event.objects.create(**event_data)

        self.stdout.write(self.style.SUCCESS(f'Sample events created for {user.username}'))

        # Create sample shopping items and lists
        shopping_items = [
            {'name': f'Item 1 for {user.username}', 'quantity': 1, 'purchased': False, 'user': user},
            {'name': f'Item 2 for {user.username}', 'quantity': 2, 'purchased': False, 'user': user},
            {'name': f'Item 3 for {user.username}', 'quantity': 3, 'purchased': False, 'user': user},
            {'name': f'Item 4 for {user.username}', 'quantity': 4, 'purchased': False, 'user': user},
            {'name': f'Item 5 for {user.username}', 'quantity': 5, 'purchased': False, 'user': user},
        ]
        items = []
        for item_data in shopping_items:
            item = ShoppingItem.objects.create(**item_data)
            items.append(item)

        shopping_list = ShoppingList.objects.create(name=f'Shopping List for {user.username}', user=user)
        shopping_list.items.set(items)

        self.stdout.write(self.style.SUCCESS(f'Sample shopping items and list created for {user.username}'))

        # Create sample reminders
        reminders = [
            {'title': f'Reminder 1 for {user.username}', 'description': f'Description for reminder 1', 'remind_at': now() + timedelta(days=1), 'user': user},
            {'title': f'Reminder 2 for {user.username}', 'description': f'Description for reminder 2', 'remind_at': now() + timedelta(days=2), 'user': user},
            {'title': f'Reminder 3 for {user.username}', 'description': f'Description for reminder 3', 'remind_at': now() + timedelta(days=3), 'user': user},
            {'title': f'Reminder 4 for {user.username}', 'description': f'Description for reminder 4', 'remind_at': now() + timedelta(days=4), 'user': user},
            {'title': f'Reminder 5 for {user.username}', 'description': f'Description for reminder 5', 'remind_at': now() + timedelta(days=5), 'user': user},
        ]
        for reminder_data in reminders:
            Reminder.objects.create(**reminder_data)

        self.stdout.write(self.style.SUCCESS(f'Sample reminders created for {user.username}'))
