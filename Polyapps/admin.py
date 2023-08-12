from django.contrib import admin
from .models import About,Contact,Specialist


# Register your models here.
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Specialist)



# To modify Django Site Administration
admin.site.site_header='MAMU MEDICS & PHYSIOTHERAPY' # default Django Administration
admin.site.index_title='MAMU PANEL'    # default Site Administration
admin.site.site_title='MAMU ADMIN'  # default Django site admin
