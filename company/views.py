from django.shortcuts import render, redirect
from .forms import CompanyModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Company, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

# Create your views here.
class CompanyListView(ListView):
	model = Company
	context_object_name = 'companies'
	template_name = 'company/companies_list.html'

class CompanyDetailView(DetailView):
	model = Company
	template_name = 'company/company_detail.html'

class CompanyCreateView(LoginRequiredMixin, CreateView):
	model = Company
	fields = ['name', 'description']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Company
	fields = ['name', 'description']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		company = self.get_object()
		if self.request.user == company.owner:
			return True
		return False

class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Company
	success_url = '/company'
	def test_func(self):
		company = self.get_object()
		if self.request.user == company.owner:
			return True
		return False


@login_required
def create_company(request):
	form = CompanyModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('company_list')
	return render(request, 'company/create_company.html', {'form': form})


class CategoryListView(ListView):
	model = Category
	template_name = 'company/category_list.html'


#class CategoryOpenDetailView(DetailView):
#	model =Category
#	template_name = 'company/open_category.html'
	