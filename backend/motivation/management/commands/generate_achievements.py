# motivation/management/commands/generate_achievements.py

from django.core.management.base import BaseCommand
from motivation.models import Achievement

achievements = [
    {'title': 'Complete 5 Tasks', 'description': 'Complete 5 tasks to earn this achievement.', 'points': 10, 'conditions': {'type': 'task_completion', 'count': 5}},
    {'title': 'Complete 10 Tasks', 'description': 'Complete 10 tasks to earn this achievement.', 'points': 15, 'conditions': {'type': 'task_completion', 'count': 10}},
    {'title': 'Complete 20 Tasks', 'description': 'Complete 20 tasks to earn this achievement.', 'points': 25, 'conditions': {'type': 'task_completion', 'count': 20}},
    {'title': 'Complete 50 Tasks', 'description': 'Complete 50 tasks to earn this achievement.', 'points': 50, 'conditions': {'type': 'task_completion', 'count': 50}},
    {'title': 'Complete 100 Tasks', 'description': 'Complete 100 tasks to earn this achievement.', 'points': 100, 'conditions': {'type': 'task_completion', 'count': 100}},
    {'title': 'First Task', 'description': 'Complete your first task to earn this achievement.', 'points': 5, 'conditions': {'type': 'task_completion', 'count': 1}},
    {'title': 'Daily Task Completion', 'description': 'Complete a task every day for a week.', 'points': 20, 'conditions': {'type': 'streak', 'days': 7}},
    {'title': 'Bi-Weekly Streak', 'description': 'Complete a task every day for two weeks.', 'points': 40, 'conditions': {'type': 'streak', 'days': 14}},
    {'title': 'Monthly Task Master', 'description': 'Complete tasks every day for a month.', 'points': 100, 'conditions': {'type': 'streak', 'days': 30}},
    {'title': 'Task Conqueror', 'description': 'Complete all your monthly goals.', 'points': 50, 'conditions': {'type': 'task_completion', 'count': 30}},
    {'title': 'Task Legend', 'description': 'Complete all your tasks for six consecutive months.', 'points': 500, 'conditions': {'type': 'streak', 'days': 180}},
    {'title': 'Quick Starter', 'description': 'Complete 3 tasks in the first day.', 'points': 10, 'conditions': {'type': 'task_completion', 'count': 3}},
    {'title': 'Morning Person', 'description': 'Complete a task before 9 AM.', 'points': 10, 'conditions': {'type': 'time_based', 'time': '09:00'}},
    {'title': 'Night Owl', 'description': 'Complete a task after 9 PM.', 'points': 10, 'conditions': {'type': 'time_based', 'time': '21:00'}},
    {'title': 'Weekend Warrior', 'description': 'Complete 5 tasks over the weekend.', 'points': 20, 'conditions': {'type': 'day_of_week', 'days': ['Saturday', 'Sunday'], 'count': 5}},
    {'title': 'Holiday Hustler', 'description': 'Complete a task on a public holiday.', 'points': 30, 'conditions': {'type': 'holiday', 'holiday': 'any'}},
    {'title': 'Efficiency Expert', 'description': 'Complete a task within 1 hour of its creation.', 'points': 15, 'conditions': {'type': 'time_based', 'time_limit': 1}},
    {'title': 'Task Marathon', 'description': 'Complete 10 tasks in a single day.', 'points': 50, 'conditions': {'type': 'task_completion', 'count': 10, 'time_limit': 24}},
    {'title': 'Quick Finisher', 'description': 'Complete a task in under 30 minutes.', 'points': 10, 'conditions': {'type': 'time_based', 'time_limit': 0.5}},
    {'title': 'Team Player', 'description': 'Complete a collaborative task.', 'points': 25, 'conditions': {'type': 'collaborative', 'collaborators': 2}},
    {'title': 'Solo Star', 'description': 'Complete 5 tasks solo.', 'points': 15, 'conditions': {'type': 'task_completion', 'count': 5, 'solo': True}},
    {'title': 'High Priority Handler', 'description': 'Complete a high-priority task.', 'points': 10, 'conditions': {'type': 'priority', 'level': 'high'}},
    {'title': 'Low Priority Manager', 'description': 'Complete 5 low-priority tasks.', 'points': 10, 'conditions': {'type': 'priority', 'level': 'low', 'count': 5}},
    {'title': 'Balanced Performer', 'description': 'Complete tasks across 3 different categories.', 'points': 20, 'conditions': {'type': 'category', 'count': 3}},
    {'title': 'Deadline Crusher', 'description': 'Complete a task before its deadline by 1 day.', 'points': 15, 'conditions': {'type': 'deadline', 'early_by': 1}},
    {'title': 'Last Minute Saver', 'description': 'Complete a task right on its deadline.', 'points': 10, 'conditions': {'type': 'deadline', 'on_time': True}},
    {'title': 'Task Overachiever', 'description': 'Complete 200 tasks.', 'points': 200, 'conditions': {'type': 'task_completion', 'count': 200}},
    {'title': 'Annual Task Champion', 'description': 'Complete 1000 tasks in a year.', 'points': 1000, 'conditions': {'type': 'task_completion', 'count': 1000, 'time_limit': 365}},
]

class Command(BaseCommand):
    help = 'Generate sample achievements'

    def handle(self, *args, **kwargs):
        for achievement_data in achievements:
            achievement, created = Achievement.objects.get_or_create(
                title=achievement_data['title'],
                defaults={
                    'description': achievement_data['description'],
                    'points': achievement_data['points'],
                    'conditions': achievement_data['conditions']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Achievement '{achievement.title}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Achievement '{achievement.title}' already exists."))
