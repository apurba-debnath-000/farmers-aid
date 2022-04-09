from django.views import generic
from Store.templatetags.cart import total_price
from Store.models.unit_type import Unit_Type
from django.db.models.query import EmptyQuerySet, QuerySet
from Store.models.categories import Category
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from .models.userprofile import UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
#for email
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .models.products import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import View, DetailView
from .models.products import Product
from .models.orders import Order
from Store.middlewares.auth import auth_middleware
from django.conf import settings
from django.core.mail import send_mail
from .templatetags.cart import *
from .templatetags.custom_filter import *
from django.contrib import messages
from .forms2 import *
from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
#-----home------
# class Index(View):

    # def post(self, request):
    #     product_id=request.POST.get('product_id')
    #     print("product ID: ",product_id)
    #     return redirect('home')

    # def get(self, request):
    #     products = None
    #     categories = Category.get_all_category()
    
    #     categoryID = request.GET.get('category_id')

    #     if categoryID:
    #         products = Product.get_all_products_by_id(categoryID)
    #     if not products:
    #         print("No item")
    #         messages.error(request, "Opps! No products are available on this category")
    #     else:
    #       products = Product.get_all_products()

    # #--paginator
    #     paginator = Paginator(products, 6)
    #     page_number = request.GET.get('page')
    #     products = paginator.get_page(page_number)


    #     data = {}
    #     data['products'] = products
    #     data['categories']= categories
    #     #return render(request, 'order.html')
    #     print('you are: ',request.session.get('current_username'))
    #     return render(request, 'store/index.html', data)

#@login_required(login_url='/login/')
def index(request):
    #Before serving index page clearing cart dict obj.
    cart = request.session.get('cart')
    if not cart:
        request.session["cart"]= {}

    products = None
    categories = Category.get_all_category()
    
    categoryID = request.GET.get('category_id')

    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
        if not products:
            print("No item")
            messages.error(request, "Opps! No products are available on this category")
    else:
        products = Product.get_all_products()
    
    if request.method == 'POST':
        product=request.POST.get('product')
        remove = request.POST.get('remove')
        #cart access in session as a cart object
        #jodi prothom theke cart na thake tobe cart object create korle ki hbe?
        cart = request.session.get('cart')# first this return None
        #Now I will check availability of cart from before or not:
        #how to logic it: using if conditions:
        if cart:
            quantity = cart.get(product)
            if quantity:
                
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                        
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart= {} #assigning empty object here
            cart[product] = 1 # 1 product add to cart

        request.session['cart'] = cart
        # print("cart:--->",request.session['cart'])

        # print("product ID: ",product)
        return redirect('home')
        

    # #--paginator
    # paginator = Paginator(products, 6)
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)


    data = {}
    data['products'] = products
    data['categories']= categories
    #return render(request, 'order.html')
    #current_user_name = request.session.get('current_username')
    # request.session.get('')
    return render(request, 'store/index.html', data)


#------------login------------
def loginPage(request, template_name='account/login.html'):
    return_url = None
    if request.method == 'GET':
        return_url = request.GET.get('return_url')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # print("the user is : ---> ",user.id)
            
            request.session['current_user_id'] = user.id
            request.session['current_username'] = user.username
            request.session['full_name'] = user.first_name
            request.session['last_name'] = user.last_name


            if return_url:
                return HttpResponseRedirect(return_url)
            else:
                return_url = None
                return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, template_name, context)

#-------Logout--------

def logoutUser(request):
    #logout(request)
    request.session.clear()
    cart = request.session.get('cart')
    if not cart:
        request.session["cart"]= {}
    return redirect('login')

#--------Sign up type---------

def typesSign(request):   
    return render(request, 'account/typeSign.html')

#---------customer registration-----
def customer_reg(request):
    form = CustomerRegForm()
    if request.method == 'POST':
        form = CustomerRegForm(request.POST)
        if form.is_valid():
            #CustomerRegForm.is_Exist_email()
            user = form.save()
            user.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+ username ) 

            return redirect('login')

    context = {'form': form}
    return render(request, 'account/cus_reg.html', context)

#---farmer registration------
def farmer_reg(request):
    
    profile_form = FarmerRegistrationForm(request.POST)
    Info_Profile_form = InfoUserProfileForm(request.POST)
    if request.method == 'POST':
        
        profile_form = FarmerRegistrationForm(request.POST)
        Info_Profile_form = InfoUserProfileForm(request.POST, request.FILES)
        
        #validation
        #phone = Info_Profile_form.cleaned_data.get('phone')
        # postData = request.POST
        # phone = postData.get('phone')
        # if len(phone) < 11 :
        #     messages.error(request, 'Phone length must be in 11 char long')
        #     return redirect(request, 'account/krishok_reg.html')
        # elif not type(phone) == int:
        #     messages.error(request, 'Character not allowed in phone no.')
        #     return redirect(request, 'account/krishok_reg.html')
        


        if profile_form.is_valid() and Info_Profile_form.is_valid():
            # print(Info_Profile_form.cleaned_data)
            user = profile_form.save()
            print("this is user: ",user)
            user.save()
            group = Group.objects.get(name='Farmer')
            user.groups.add(group)

            # profile = Info_Profile_form.save(commit=False)
            profile = user.userprofile
            profile.address = Info_Profile_form.cleaned_data.get('address', None)
            profile.national_id_no = Info_Profile_form.cleaned_data.get('national_id_no', None)
            profile.phone = Info_Profile_form.cleaned_data.get('phone', None)
            #profile.user = user
            
            if request.FILES:
                print('Yes')
                img = request.FILES['image']
                profile.image.save(img.name, img, save=True)
                nimg = request.FILES['national_id']
                profile.national_id.save(nimg.name, nimg, save=True)

            profile.save()

            username = profile_form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+ username ) 
            return redirect('login')
        
    context = {
        'profile_form':profile_form, 
        'Info_Profile_form':Info_Profile_form
        }
    return render(request, 'account/krishok_reg.html', context)        

#Agriculture_officer
def agri_officer_reg(request):
    
    profile_form = FarmerRegistrationForm(request.POST)
    Info_Profile_form = InfoUserProfileForm(request.POST)
    if request.method == 'POST':
        
        profile_form = FarmerRegistrationForm(request.POST)
        Info_Profile_form = InfoUserProfileForm(request.POST, request.FILES)
        print(request.FILES)
        


        if profile_form.is_valid() and Info_Profile_form.is_valid():
            print(Info_Profile_form.cleaned_data)
            user = profile_form.save()
            print("this is user: ",user)
            user.save()
            group = Group.objects.get(name='Agri_officer')
            user.groups.add(group)

            # profile = Info_Profile_form.save(commit=False)
            profile = user.userprofile
            profile.address = Info_Profile_form.cleaned_data.get('address', None)
            profile.national_id_no = Info_Profile_form.cleaned_data.get('national_id_no', None)
            profile.phone = Info_Profile_form.cleaned_data.get('phone', None)
            #profile.user = user
            
            if request.FILES:
                print('Yes')
                img = request.FILES['image']
                profile.image.save(img.name, img, save=True)
                nimg = request.FILES['national_id']
                profile.national_id.save(nimg.name, nimg, save=True)

            profile.save()

            username = profile_form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+ username ) 
            return redirect('login')
        
    context = {
        'profile_form':profile_form, 
        'Info_Profile_form':Info_Profile_form
        }
    return render(request, 'account/agri_officer_reg.html', context)  

    
def return_login(request):
    user = request.session.get('current_user_id')
    if not user:
        return redirect('login')

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        print("here is:--",ids)
        products = Product.get_product_by_ids(ids)
        print('All products:---->> ', products)
        context = {"products":products}
        return render(request, 'store/cart.html',context )

class Checkout(View):
    def post(self, request):
        user = request.session.get('current_user_id')
        username = request.session.get('current_username')
        first_name = request.session.get('full_name')
        last_name = request.session.get('last_name')
        
        #print(username)
        
        if not user:
            return redirect('login')
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        email = request.POST.get('email')
        cart = request.session.get('cart')
       
        products = Product.get_product_by_ids(list(cart.keys()))

        
        
        #now we just have to get price, unit_type, and quantity
        counter = 0 
        totalProduct = 0 

        for p in products:
            totalProduct = totalProduct+1
            total_quantity = p.quantity
            cart_products = cart.get(str(p.id))
            # print("Total_quantity: ----->",total_quantity)
            # print("cart_quantity: ----->",cart_products)
            if total_quantity < cart_products:
                messages.error(request, "Sorry! Stock is not available for this product named:---->> "+str(p.name)+".    Availability is: ----->>>"+ str(p.quantity))
                return redirect('cart' )
            else:

                p.quantity = p.quantity - cart_products
                
                p.save()
                # print("save product: ",p.quantity )
                order = Order(
                            user = User(id=user),
                            product = p,
                            price = p.Unit_price,
                            address = address,
                            phone = phone,
                            email = email,

                            quantity = cart_products,
                            unit = p.unit
                )
                
                order.save()
                date = order.date
                
                # print("""
                # Your order has been saved successfully.
                # Thank You for being with us. Please check your email as order confirmation.
                
                # """)
           
            #counter = counter+1
        #p.quantity -cart.get(str(p.id))
        #Sending email:------------------------>

        # errorMessage = "" 
        
        # if counter != totalProduct:
        #     errorMessage = "Sorry " + str(totalProduct - counter) + " of the products are not available in STOCk!"

        # if counter != 0:
        total = cart_total_price(products,cart)
        curr = currency(total)
        # print("Total price:-->>",total)
        # print(" curreency : -->>",curr)

        #Email_code:
        context = {
            'first_name': first_name,
            'last_name':last_name,
            'username':username,
            'curr': curr,
            'date': date,
            'address':address,
            'phone': phone,



        }
        template = render_to_string('store/email_template.html', context)
        email = EmailMessage(
            ' Order Confirmation: from farmer-aids.com, Thanks for purchasing our   products!! ',
            template,
            settings.EMAIL_HOST_USER,
            [email]


        )
        email.fail_silenty = False
        email.send()


        # subject = 'Order Confirmation:--> eKrishok.com'
        # message = f'''
        #     Hello, {username}. You have ordered total : {curr} from eKrishok.com.Your order has taken succesfully , you will get your desire products within 3 days. 
                    
                    
        #             '''
        # email_from = settings.EMAIL_HOST_USER

        # recipient_list = [email]

        #         #----Sending email-------
        # send_mail(subject, message, email_from, recipient_list)
                    # print("All data @--->",address,phone,email,user)
                    # print('products: ', products, 'cart is: ', cart)
        
        request.session['cart'] = {}
        messages.error(request, """--
        Your order has placed successfully
         ----  Thank You for being with us..
         -----  Please! Chaeck your email as order confirmation...

        --""")
        return redirect('cart' )
        


class OrderView(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        user = request.session.get("current_user_id")
        orders = Order.get_orders_by_user(user)
        # print(orders)
        return render(request, 'store/order.html',{"orders":orders} )


class ViewProduct(DetailView):
    queryset = Product.objects.all()
    products = Product.get_all_products()
    template_name = 'store/pro_details.html'

class ViewFarmer(DetailView):
   
    queryset = User.objects.all().select_related('userprofile')
    #  def get(self, request):
    #     users = User.objects.all().select_related('profile')
    #     return render(request, 'store/farmer_details.html', {'users': users})
    
    
    template_name = 'store/farmer_details.html'

    # def get_queryset(self):
    #     return UserProfile.objects.all()



def profile_view(request):
    user = request.session.get('current_user_id')
    data = UserProfile.get_info_of_user(user)
    #user = User.objects.filter(User, id = user)
    # print(data)
    context = {
        'data':data
    }
    
    return render(request, 'profile/profile.html',context)

def edit_profile(request):
    user = request.session.get('current_user_id')
    data = UserProfile.get_info_of_user(user)

    if request.method == 'POST':
        p_form = InfoUserProfileForm(request.POST,  request.FILES,
        instance=request.user.userprofile, 
        
        )

        u_form = User_Form(request.POST, 
        instance= request.user)

        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            #user.set_password(user.password1)
            user.save()
            group = Group.objects.get(name='Farmer')
            user.groups.add(group)

            profile = p_form.save(commit=False)
            profile.user = user
            # if request.FILES:
            #     profile.image = request.FILES['image'] 
            #     profile.national_id = request.FILES['national_id']

            profile.save()

            username = u_form.cleaned_data.get('username')
            messages.success(request, 'Account updated successfully for '+ username ) 
            return redirect('profile')


    else:
        p_form = InfoUserProfileForm(instance=request.user.userprofile)

        u_form = User_Form(instance= request.user)

    context = {
    "p_form":p_form,
    "u_form": u_form,
    'data': data,
    
    }
    return render(request, 'profile/edit_pro.html', context)

# class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    #success_url = reverse_lazy('profile')
    success_url = reverse_lazy('password_success')



def password_success(request):
    return render(request, 'profile/password_success.html', {})



#-----------Extra code---farmer registration--works--------

#--------Farmer registration----------######
# def farmer_reg(request):
#     register = False
#     error_message= None

#     if request.method == 'POST':
#         profile_form = FarmerRegistrationForm(data=request.POST)
#         Info_Profile_form = InfoUserProfileForm(data=request.POST)

#         # if(not User.first_name):
#         #     error_message = "First name required"
#         # elif(not User.last_name):
#         #     error_message = "Last name required"
#         # elif(not User.email):
#         #     error_message = "Email required"
#         # elif len(UserProfile.phone) < 11:
#         #     error_message = "Phone no must be 11 char long"
#         # # print(Info_Profile_form)
        
#         if profile_form.is_valid() and Info_Profile_form.is_valid():
#             user = profile_form.save()
#             user.save()

#             group = Group.objects.get(name='Farmer')
#             user.groups.add(group)


#             profile = Info_Profile_form.save(commit=False)
#             profile.user = user
#             if request.FILES:
#                 profile.image = request.FILES['image']
#                 profile.national_id = request.FILES['national_id']

#             profile.save()
#             print("success")
#             register = True
#         else:
#             return HttpResponse("<h1>Something went wrong with from</h1>")
#     else:
        
#         profile_form = FarmerRegistrationForm(data=request.POST)
#         Info_Profile_form = InfoUserProfileForm(data=request.POST)
        
        
        

    # return render(request, 'krishok_reg.html', {
    #     'profile_form':profile_form, 
    #     'Info_Profile_form':Info_Profile_form,
    #     'register': register,
    #     # 'error': error_message,
        
    #     }) 
