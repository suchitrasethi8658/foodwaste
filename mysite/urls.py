from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mysite.core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('add/new/', core_views.addnew, name='addnew'),
    path('add/orphanage-details/', core_views.addorphan, name='addorphan'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/agent/', auth_views.LoginView.as_view(template_name='login.html'), name='agentlogin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('signup/agent/', core_views.signupag, name='signupag'),
    path('update/<int:pk>', core_views.updates, name='update_det'),
    path('delete/<int:pk>', core_views.deletes, name='delete_det'),
    path('updateorp/<int:pk>', core_views.updateorp, name='update_orp_det'),
    path('deleteorp/<int:pk>', core_views.deleteorp, name='delete_orp_det'),
    path('orphanage/', core_views.orphangaedets, name='orphanagedet'),
    path('allocate/<int:pk>', core_views.allocatedet, name='allocate_dets'),
    path('architecture/', core_views.archi, name='archi'),
    path('charts/<str:chart_type>/<str:cha_type>/', core_views.chartsview, name='charts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
