from rest_framework import serializers

from motivation.models import Achievement, UserAchievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['uuid', 'title', 'description', 'points', 'conditions']


class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserAchievement
        fields = ['uuid', 'achievement', 'user', 'date_earned', 'is_notified']
