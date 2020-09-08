from django.contrib.auth.models import BaseUserManager

class AuthManager(BaseUserManager):
    def create_user(self, email, staff_ID, password=None):
        """
        create and save staff with given ID
        """
        if not staff_ID:
            raise ValueError("Please enter a valid staff ID and Email")

        user = self.model(
            email = self.normalize_email(email),
            staff_ID = staff_ID,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, staff_ID, password=None):
        """
        Create superuser with email
        """
        user = self.create_user(
            email,
            password=password,
            staff_ID = staff_ID,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user