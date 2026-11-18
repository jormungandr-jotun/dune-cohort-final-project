from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import InquiryForm, PropertyForm
from .models import Property, SavedProperty

def home(request):
    featured = Property.objects.filter(status="available")[:6]
    return render(request, "listings/home.html", {"featured": featured})

def property_list(request):
    query = request.GET.get("q", "").strip()
    properties = Property.objects.filter(status="available")
    if query:
        properties = properties.filter(Q(title__icontains=query) | Q(city__icontains=query) | Q(address__icontains=query))
    return render(request, "listings/property_list.html", {"properties": properties, "query": query})

def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    inquiry_form = InquiryForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.info(request, "Please log in to contact the listing owner.")
            return redirect("login")
        inquiry_form = InquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry = inquiry_form.save(commit=False)
            inquiry.property = property_obj
            inquiry.sender = request.user
            inquiry.save()
            messages.success(request, "Your inquiry has been sent.")
            return redirect(property_obj.get_absolute_url())
    return render(request, "listings/property_detail.html", {"property": property_obj, "inquiry_form": inquiry_form})

@login_required
def dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, "listings/dashboard.html", {"properties": properties})

@login_required
def property_create(request):
    form = PropertyForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        property_obj = form.save(commit=False)
        property_obj.owner = request.user
        property_obj.save()
        messages.success(request, "Your property listing has been created.")
        return redirect("dashboard")
    return render(request, "listings/property_form.html", {"form": form, "page_title": "Add a property"})

@login_required
def property_update(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    if property_obj.owner != request.user and not request.user.is_staff:
        raise Http404
    form = PropertyForm(request.POST or None, request.FILES or None, instance=property_obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your property listing has been updated.")
        return redirect("dashboard")
    return render(request, "listings/property_form.html", {"form": form, "page_title": "Edit property"})

@login_required
def property_delete(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    if property_obj.owner != request.user and not request.user.is_staff:
        raise Http404
    if request.method == "POST":
        property_obj.delete()
        messages.success(request, "The property listing has been deleted.")
        return redirect("dashboard")
    return render(request, "listings/property_confirm_delete.html", {"property": property_obj})

@login_required
def save_property(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    SavedProperty.objects.get_or_create(user=request.user, property=property_obj)
    messages.success(request, "Property saved to your favourites.")
    return redirect(property_obj.get_absolute_url())

@login_required
@user_passes_test(lambda user: user.is_staff)
def staff_inquiries(request):
    inquiries = __import__("listings.models", fromlist=["Inquiry"]).Inquiry.objects.select_related("property", "sender")
    return render(request, "listings/staff_inquiries.html", {"inquiries": inquiries})
