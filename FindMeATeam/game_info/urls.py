from django.urls import path
from . import views
from .views import GameInfoCreateView, GameInfoListView, GameInfoDetailView, UserGamesList, GameInfoUpdateView, GameInfoDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', GameInfoListView.as_view(), name='home'),
	path('create/', GameInfoCreateView.as_view(), name='create'),
	path('view/<int:pk>/', GameInfoDetailView.as_view(), name='view'),
	path('view/user/<str:username>/', UserGamesList.as_view(), name='view-user'),
	path('update/<int:pk>/', GameInfoUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', GameInfoDeleteView.as_view(), name='delete')
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)