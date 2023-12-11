from django.db import models

# Create your models here.


class Menu(models.Model):
    """
    Models for menu
    """
    menu_id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True, null=True)

    depth = models.IntegerField()
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["depth"]


    def get_absolute_url(self):
        """
        Returns the url to access a particular menu instance
        """
        pass

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f"{self.title}"