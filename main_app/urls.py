from djang.urls import path
from . import views
url patterns = [
    path('admin/', admin.site.urls), 
    path('', include('main_app.urls'))
]