from django.db import models

# This model tracks visits to different pages of the website
class PageVisit(models.Model):
    # Stores the URL path of the visited page.
    # The 'blank=True' and 'null=True' options allow the field to be optional.
    path = models.TextField(blank=True, null=True)

    # Automatically records the timestamp when a new page visit record is created.
    # 'auto_now_add=True' sets this field to the current datetime when the object is created.
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Optional: You can define a string representation of the model for easier identification in Django admin or shell.
    def __str__(self):
        return f"Visited {self.path} on {self.timestamp}"
