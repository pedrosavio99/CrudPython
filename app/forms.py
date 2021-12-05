from django.forms import ModelForm
from app.models import motos


class MotosForm(ModelForm):
    class Meta:
        model = motos
        fields = ['modelo','marca','preço']