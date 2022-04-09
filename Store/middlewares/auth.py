from django.shortcuts import redirect
def auth_middleware(get_response):
   
    def middleware(request):
        returnUrl= request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        user = request.session.get('current_user_id')
        if not user :
            return redirect(f'/login/?return_url={returnUrl}')
        
        print("this is middleware",middleware)
        response = get_response(request)
        return response

    return middleware