from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='_id')
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id')
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='_id')
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
