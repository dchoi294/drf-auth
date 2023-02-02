# We want our model to be accessible from the Django Admin panel
from django.contrib import admin
# import our models
from .models import Practice


# register the model
admin.site.register(Practice)
