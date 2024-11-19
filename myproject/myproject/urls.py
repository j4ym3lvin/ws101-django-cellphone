from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cellphones/', include('cellphones.urls')),  # Include the cellphone app's URLs
    path('', RedirectView.as_view(url='/cellphones/', permanent=True)),  # Redirect root to cellphone list
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),  # Home page
]