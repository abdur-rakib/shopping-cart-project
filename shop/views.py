from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Product, Comment
from cart.forms import CartAddProductForm
from .forms import CommentForm
from django.contrib import messages



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 8)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/home.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    category = product.category
    products = Product.objects.filter(category=category)[:3]
    cart_product_form = CartAddProductForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            messages.success(request, 'Comment posted successfully.')
            return redirect('shop:product_detail', id=product.id, slug=product.slug)
    else:
        comment_form = CommentForm()

    return render(request, 'shop/product-detail.html', {'product': product, 'products': products, 'cart_product_form': cart_product_form, 'comment_form': comment_form})
