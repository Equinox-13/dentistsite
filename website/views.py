from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message = request.POST['message']
        print("message_name==========>", message_name )
        print("message_phone==========>", message_phone )
        print("message_email==========>", message_email )
        print("message==========>", message )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})
