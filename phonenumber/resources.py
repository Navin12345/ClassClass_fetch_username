from import_export import resources
from student.models import UserProfile

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
