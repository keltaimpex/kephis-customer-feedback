from django.db import models

class CustomerFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)
    specific_service = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    office = models.CharField(max_length=100)

    # Ratings
    rating_working_environment = models.IntegerField(null=True, blank=True)
    rating_courtesy = models.IntegerField(null=True, blank=True)
    rating_professionalism = models.IntegerField(null=True, blank=True)
    rating_waiting_time = models.IntegerField(null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
