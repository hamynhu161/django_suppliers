from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

# Product views
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render(request, 'productlist.html', context)

#Add-product views
def addproduct(request):
    a = request.POST['productName']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']

    Product(productName = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id=e)).save()
    return redirect(request.META['HTTP_REFERER'])

# Supplier views
def supplierlistview(request):
    supplierlist = Supplier.objects.all()        
    context = {'suppliers': supplierlist}               # create dictionary called context with key:suppliers, value: supplierlist
    return render(request, 'supplierlist.html', context)

# Add-supplier views
def addsupplier(request):
    a =request.POST['companyName']
    b =request.POST['contactName']
    c =request.POST['address']
    d =request.POST['phone']
    e =request.POST['email']
    f =request.POST['country']
    Supplier(companyName = a, contactName = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])           #This gets the URL of the previous page — the page where the form was submitted from.