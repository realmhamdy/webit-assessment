from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from python_test.forms import ClientForm, ClientSearchForm
from python_test.models import Client, Address


class CreateClientView(CreateView):

    form_class = ClientForm
    template_name = "create_client.html"
    success_url = reverse_lazy("list_client")


class UpdateClientView(UpdateView):

    form_class = ClientForm
    template_name = "update_client.html"
    success_url = reverse_lazy("update_client")
    queryset = Client.objects.all()


class ClientListView(ListView):

    template_name = "client_list.html"
    context_object_name = "clients"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["search_form"] = ClientSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        name_q = self.request.GET.get("name", "")
        email_q = self.request.GET.get("email", "")
        phone_q = self.request.GET.get("phone", "")
        suburb_q = self.request.GET.get("suburb", "")
        order_by_field = self.request.GET.get("order_by", "id")
        queryset = Client.objects.filter(
                    name__icontains=name_q, email__icontains=email_q, phone__icontains=phone_q)\
                .order_by(order_by_field)
        if suburb_q:
            queryset = queryset.filter(address__suburb__icontains=suburb_q)
        return queryset
    