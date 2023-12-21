from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    jersey_number = models.PositiveIntegerField()
    birthdate = models.DateField()
    batting_throwing = models.CharField(max_length=10)
    

    # Change height field to a CharField
    height = models.CharField(max_length=10)

    # Fields for height and weight as integers
    weight = models.PositiveIntegerField()  # Weight in pounds
    
    # Optional statistics for hitters
    avg = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    home_runs = models.PositiveIntegerField(blank=True, null=True)
    
    # Fields for pitching records and ERA as integers
    pitching_wins = models.PositiveIntegerField(blank=True, null=True)
    pitching_losses = models.PositiveIntegerField(blank=True, null=True)
    era = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)  # ERA as a decimal
    
    hometown = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    class_standing = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.jersey_number} - {self.first_name} {self.last_name}"

