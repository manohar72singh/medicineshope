from django import forms

class AddNewCustomerForm(forms.Form):
    cn = forms.CharField(label="Custoner NAme",max_length=50)
    em =forms.EmailField(label="Email",max_length=100)
    mob = forms.IntegerField(label="Mobile Number")
    gen = forms.CharField(label="Gender")
    addr = forms.CharField(label="Address")


class AddNewMedicineForm(forms.Form):
    mn = forms.CharField(label="Medicine Name", max_length=50)
    mfg = forms.DateField(label="Mfg Date")
    batch = forms.CharField(label="Batch No",max_length=8)
    exp = forms.DateField(label="Exp Date")
    comp = forms.CharField(label="Company Name", max_length=50)
    mrp = forms.IntegerField(label="Mrp")

