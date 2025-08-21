from django import forms
from .models import Trade


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = [
            'symbol', 'side', 'quantity', 'entry_price', 'exit_price',
            'entry_time', 'exit_time', 'notes'
        ]
        widgets = {
            'entry_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'exit_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
