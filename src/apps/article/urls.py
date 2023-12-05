from django.urls import path, include

from . views import ListArticle

# urlarticle = ([
#     path('<int:pk>', pass),
# ], 'article')

urlcategories = ([
    path('<int:cat_id>', ListArticle.as_view()),
], 'category')

urlpatterns = [
    path('category/', include(urlcategories)),
]
