from django import forms

class trackingForm(forms.Form):
    tracking_id = forms.CharField(label=False,max_length=30,widget=forms.TextInput(
            attrs={
                
                'placeholder':'Enter a tracking number',
                'label':'',
            }
        ))
    
    

    def clean(self):
        cleaned_data = super(trackingForm, self).clean()
        id = cleaned_data.get('tracking_id')

