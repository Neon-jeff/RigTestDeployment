from django.shortcuts import render
from .models import *
# Create your views here.

def Shop_Books(request):
    book_items=ShopItem.objects.filter(item_type='book')
    work_book=ShopItem.objects.filter(item_type='work-book')
    limited_items=ShopItem.objects.filter(item_type='limited')
    return render(request,'shop-books.html',{'books':book_items,'workbooks':work_book,'limited':limited_items})

def Shop_Merchs(request):
    merch_items=ShopItem.objects.filter(item_type='merch')
    limited_items=ShopItem.objects.filter(item_type='limited')
    return render(request,'shop-merch.html',{'merchs':merch_items,'limited':limited_items})
