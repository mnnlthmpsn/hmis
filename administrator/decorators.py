from django.contrib.auth.decorators import user_passes_test, login_required

user_auth_required = user_passes_test(lambda user: user.profile.role.name == 'Administrator', login_url='/')

def admin_user_required(view_func):
    decorated_view_func = login_required(user_auth_required(view_func))
    return decorated_view_func