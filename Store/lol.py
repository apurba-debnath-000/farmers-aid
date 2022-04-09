#--------Farmer registration----------######
def farmer_reg(request):
    register = False
    error_message= None
    
    if request.method == 'POST':
        profile_form = FarmerRegForm(data=request.POST)
        Info_Profile_form = InfoUserProfileForm(data=request.POST)

        # if(not User.first_name):
        #     error_message = "First name required"
        # elif(not User.last_name):
        #     error_message = "Last name required"
        # elif(not User.email):
        #     error_message = "Email required"
        # elif len(UserProfile.phone) < 11:
        #     error_message = "Phone no must be 11 char long"
        # # print(Info_Profile_form)
        
        if profile_form.is_valid() and Info_Profile_form.is_valid():
            user = profile_form.save()
            user.save()

            group = Group.objects.get(name='Farmer')
            user.groups.add(group)


            profile = Info_Profile_form.save(commit=False)
            profile.user = user
            if request.FILES:
                profile.image = request.FILES['image']
                profile.national_id = request.FILES['national_id']

            profile.save()

            print("success")
            register = True
        else:
            return HttpResponse("<h1>Something went wrong with from</h1>")
    else:
        
        profile_form = FarmerRegForm(data=request.POST)
        Info_Profile_form = InfoUserProfileForm(data=request.POST)
        
        
        

    return render(request, 'krishok_reg.html', {
        'profile_form':profile_form, 
        'Info_Profile_form':Info_Profile_form,
        'register': register,
        # 'error': error_message,
        
        }) 