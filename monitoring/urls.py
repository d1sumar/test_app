from django.urls import path

from monitoring.views import subjects_view, variants_view, subject_list_view, result_view, result_list_view, \
    VariantCreateView

app_name = "monitoring"
urlpatterns = [
    path('subjects/', subject_list_view, name="subject_list"),
    path('subjects/<int:pk>/', subjects_view, name="subjects"),
    path('variants/<int:pk>/', variants_view, name="variants"),
    path('results/', result_list_view, name="result_list"),
    path('results/<int:pk>/', result_view, name="result"),

    # Teachers
    path('variants/create/', VariantCreateView.as_view(), name="variant_create"),
]

