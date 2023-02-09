from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path as url
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, SetPasswordResetForm

urlpatterns = [
                  url(r'^$', views.HomeView.as_view(), name='home'),
                  url(r'^product-detail/(?P<id>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),
                  url(r'^tshart/$', views.TShartView.as_view(), name='tshart'),
                  url(r'^tshart/(?P<data>[\w-]+)/$', views.TShartView.as_view(), name='tshartdata'),
                  url(r'^jeans/$', views.JeansView.as_view(), name='jeans'),
                  url(r'^jeans/(?P<data>[\w-]+)/$', views.JeansView.as_view(), name='jeansdata'),
                  url(r'^shoes/$', views.ShoesView.as_view(), name='shoes'),
                  url(r'^shoes/(?P<data>[\w-]+)/$', views.ShoesView.as_view(), name='shoesdata'),
                  url(r'^top/$', views.TOpWearView.as_view(), name='top'),
                  url(r'^top/(?P<data>[\w-]+)/$', views.TOpWearView.as_view(), name='topdata'),
                  url(r'^bottom/$', views.BottomWearView.as_view(), name='bottom'),
                  url(r'^bottom/(?P<data>[\w-]+)/$', views.BottomWearView.as_view(), name='bottomdata'),
                  url(r'^bra/$', views.BraView.as_view(), name='bra'),
                  url(r'^bra/(?P<data>[\w-]+)/$', views.BraView.as_view(), name='bradata'),
                  url(r'^lshoes/$', views.LShoesView.as_view(), name='lshoes'),
                  url(r'^lshoes/(?P<data>[\w-]+)/$', views.LShoesView.as_view(), name='lshoesdata'),
                  url(r'^add-to-cart/$', views.AddToCartView.as_view(), name='add-to-cart'),
                  url(r'^cart/$', views.ShowCartView.as_view(), name='showcart'),
                  url(r'^pluscart/$', views.PlusCartView.as_view(), name='pluscart'),
                  url(r'^minuscart/$', views.MinusCartView.as_view(), name='minuscart'),
                  url(r'^removecart/$', views.RemoveCartView.as_view(), name='removecart'),
                  path('buy/', views.buy_now, name='buy-now'),
                  url(r'^profile/$', views.CustomerProfileView.as_view(), name='profile'),
                  url(r'^address/$', views.CustomerAddressView.as_view(), name='address'),
                  url(r'^orders/', views.OrderView.as_view(), name='orders'),
                  url(r'^checkout/', views.CheckoutView.as_view(), name='checkout'),
                  url(r'^paymentdone/', views.PaymentdonetView.as_view(), name='paymentdone'),
                  url(r'^changepassword/$', auth_views.PasswordChangeView.as_view(
                      template_name='product/changepassword.html', form_class=MyPasswordChangeForm,
                      success_url='/passwordchangedone/'),
                      name='changepassword'),
                  url(r'^passwordchangedone/$',
                      auth_views.PasswordChangeDoneView.as_view(template_name='product/passwordchangedone.html'),
                      name='passwordchangedone'),
                  url(r'^reset_password/$',
                      auth_views.PasswordResetView.as_view(template_name='product/resetpassword.html',
                                                           form_class=MyPasswordResetForm), name='password_reset'),
                  url(r'^reset_password/done/$',
                      auth_views.PasswordResetDoneView.as_view(template_name='product/reset_password_done.html'),
                      name='password_reset_done'),
                  url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                      auth_views.PasswordResetConfirmView.as_view(template_name='product/reset_password_conform.html',
                                                                  form_class=SetPasswordResetForm),
                      name='password_reset_confirm'),
                  url(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(
                      template_name='product/reset_password_complate.html'), name='password_reset_complete'),
                  url(r'^registration/$', views.CustomerRegistrationView.as_view(), name='customerregistration'),
                  url(r'^accounts/login/$',
                      auth_views.LoginView.as_view(template_name='product/login.html', authentication_form=LoginForm),
                      name='login'),
                  url(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  url(r'^search/$', views.SearchView.as_view(), name='search')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
