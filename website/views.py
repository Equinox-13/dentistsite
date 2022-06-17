from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send an email
        send_mail(subject=message_name,
                  message=message,
                  from_email=message_email,
                  recipient_list=['quaid.johar33@gmail.com'],
                  )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def departments(request):
    return render(request, 'departments.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def appointment(request):
    if request.method == "POST":
        appointment_name = request.POST['appointment-name']
        appointment_phone = request.POST['appointment-phone']
        appointment_email = request.POST['appointment-email']
        appointment_address = request.POST['appointment-address']
        appointment_date = request.POST['appointment-date']
        appointment_time = request.POST['appointment-time']
        appointment_message = request.POST['appointment-message']

        appointment_body = "Name: " + appointment_name +\
                           "Phone: " + appointment_phone +\
                           "Email: " + appointment_email +\
                           "Address: " + appointment_address +\
                           "Date: " + appointment_date +\
                           "Time: " + appointment_time +\
                           "Message: " + appointment_message
        # Send an email
        send_mail(subject="Appointment Request",
                  message=appointment_body,
                  from_email=appointment_email,
                  recipient_list=['quaid.johar33@gmail.com'],
                  )

        return render(request, 'appointment.html',
                      {'appointment_name': appointment_name,
                       'appointment_phone': appointment_phone,
                       'appointment_email': appointment_email,
                       'appointment_address': appointment_address,
                       'appointment_date': appointment_date,
                       'appointment_time': appointment_time,
                       'appointment_message':appointment_message,
                       })
    else:
        return render(request, 'home.html', {})