from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)


from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories


class CatalogCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.creator = user
        product.save()

        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


    def get_form_class(self):
        user = self.request.user
        moderator_permissions = [
            user.has_perm("catalog.set_published"),
            user.has_perm("catalog.edit_description"),
            user.has_perm("catalog.change_category_product")
        ]
        if self.object.creator == user:
            return ProductForm
        if all(moderator_permissions):
            return ProductModeratorForm
        raise PermissionDenied




class CatalogListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        category_id = self.request.GET.get('category_id')
        data = super().get_queryset().order_by('-created_at')
        if category_id:
            data = data.filter(category_id=category_id).order_by('-created_at')
            return data
        queryset = data.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        category_id = self.request.GET.get('category_id')
        data = super().get_context_data()
        data["object_list"] = [
            {
                "product": item,
                "version": item.version_set.filter(
                    current_version_indicator=True
                ).first(),
            }
            for item in data["object_list"]
        ]
        data['categories'] = get_categories()
        data['category'] = get_object_or_404(Category, id=category_id) if category_id else None
        return data


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Product
    success_url = reverse_lazy("catalog:product")


class ContactTemplateView(TemplateView):
    template_name = "contacts.html"

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"{name} {phone} {message}")
        return render(request, "contacts.html")
