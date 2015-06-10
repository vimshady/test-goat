from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^lists/(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
    # url(r'^admin/', include(admin.site.urls)),
]

