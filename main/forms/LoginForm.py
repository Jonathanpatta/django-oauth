from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):
    template_name = "Login.html"

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)