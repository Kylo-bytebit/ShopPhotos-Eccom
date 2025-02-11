from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShopPhotos
from django.contrib.admin.views.decorators import staff_member_required
from shopphotos.models import ShopPhotos
from members.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm,PaymentForm
from .models import Image
from django.contrib import messages


def home(request):
    shopphotos = ShopPhotos.objects.all()
    context = {'shopphotos': shopphotos}
    return render(request, 'home.html', context)

def search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        photos = ShopPhotos.objects.filter(name__contains=searched)
        return render(request, 'search.html',{'searched':searched, 'photos':photos })
    else:
        return render(request, "search.html")
    


@login_required
def upload_image(request):
    form_class = ImageUploadForm
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})




def add_to_cart(request, photo_id):
    """
    Add a photo to the user's cart.
    
    Args:
        request (HttpRequest): The current request object.
        photo_id (int): The ID of the photo to be added to the cart.
        
    Returns:
        HttpResponse: A redirect to the cart page.
    """
    # Get the photo object
    photo = ShopPhotos.objects.get(id=photo_id)
    
    # Check if the photo is in stock
    if photo.stock > 0:
        # Add the photo to the cart
        cart = request.session.get('cart', {})
        if photo_id in cart:
            cart[photo_id]['quantity'] += 1
        else:
            cart[photo_id] = {
                'name': photo.name,
                'price': photo.price,
                'quantity': 1
            }
        request.session['cart'] = cart
        
        # Update the stock
        photo.stock -= 1
        photo.save()
        
        messages.success(request, f"{photo.name} has been added to your cart.")
    else:
        messages.error(request, f"{photo.name} is currently out of stock.")
    
    return redirect('cart')[1]


def image_purchase_v (request, image_title):
     
    image = get_object_or_404(Image, title=image_title)   
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment here
            card_number = form.cleaned_data['card_number']
            expiry = form.cleaned_data['expiry']
            cvc = form.cleaned_data['cvc']
            
            # Dummy payment processing
            print(f'Processing payment with card: {card_number}, {expiry}, {cvc}')
            
            # Redirect to success page or show success message
            return render(request, 'Home')
    else:
        form = PaymentForm()
    
    return render(request, 'purchase copy.html', {'image': image})




def image_purchase(request, image_name):
    image = get_object_or_404(ShopPhotos, name=image_name)   
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment here
            card_number = form.cleaned_data['card_number']
            expiry = form.cleaned_data['expiry']
            cvc = form.cleaned_data['cvc']
            
            # Dummy payment processing
            print(f'Processing payment with card: {card_number}, {expiry}, {cvc}')
            
            # Redirect to success page or show success message
            return render(request, 'Home')
    else:
        form = PaymentForm()
    
    return render(request, 'purchase copy.html', {'image': image})
    
@login_required
def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id, user=request.user)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm(instance=image)
    return render(request, 'edit_image.html', {'form': form, 'image': image})

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id, user=request.user)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'delete_image.html', {'image': image})