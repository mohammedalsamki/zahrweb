from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InKindDonation, CashDonation, Idea, CustomUser


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "placeholder": "John Doe",
                "maxlength": "16",
                "minlength": "6",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "email",
                "id": "email",
                "type": "email",
                "placeholder": "JohnDoe@mail.com",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "password1",
                "id": "password1",
                "type": "password",
                "placeholder": "password",
                "maxlength": "22",
                "minlength": "8",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "password2",
                "id": "password2",
                "type": "password",
                "placeholder": "password",
                "maxlength": "22",
                "minlength": "8",
            }
        )
        self.fields["phoneNumber"].widget.attrs.update(
            {
                "class": "form-input",
                "required": "",
                "name": "phoneNumber",
                "id": "phoneNumber",
                "type": "number",
                "placeholder": "JohnDoe@mail.com",
            }
        )

    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "is_naf",
            "phoneNumber",
        )


# # forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, required=True)
#     phoneNumber = forms.CharField(max_length=200, required=False)

#     class Meta:
#         model = CustomUser
#         fields = (
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#             "is_naf",
#             "is_teacher",
#             "mailing_address",
#             "phoneNumber",
#             "RegisterDate",
#             "FamilyNumbers",
#             "NationalNumber",
#             "nationality",
#         )


class InKindDonationForm(forms.ModelForm):
    class Meta:
        model = InKindDonation
        fields = (
            "Name",
            "Email",
            "PhoneNumber",
            "Country",
            "TypeOfDonation",
            "AmountOfDonation",
        )


class CashDonationForm(forms.ModelForm):
    class Meta:
        model = CashDonation
        fields = ("Name", "Email", "PhoneNumber", "Country", "Cash")


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = (
            "idea",
            "name",
            "PhoneNumber",
        )
