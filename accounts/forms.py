from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# check out docs on this django.contrib.auth

class UserCreateForm(UserCreationForm):

    # sta attento che questa classe non abbia nome uguale da quella da cui eredita
    
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        # questi quattro campi ('username', 'email', 'password1', 'password2') vengono da django.contrib.auth

        model = get_user_model()

        def __init__(self, *args, **kwargs):
            # **kwargs vuol dire keywords argumentts
            super().__init__(*args,**kwargs)

            # customizzazione di
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'

            # anche con errori rossi funziona lo stesso


        