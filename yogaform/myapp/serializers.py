from .models import *
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
class FormSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    contact_number = serializers.CharField() 
    gender=serializers.CharField()
    batch_id=serializers.IntegerField()
    amount=serializers.IntegerField()
    payment_successful=serializers.BooleanField()

    def save(self):
        print("hello save")
        f_name=self.get('first_name')
        l_name=self.get('last_name')
        a=self.get('age')
        e=self.get('email')
        cn=self.get('contact_number')
        g=self.get('gender')
        b=self.get('batch_id')
        amt=self.get('amount')
        p=self.get('payment_successful')
        print(a,e,cn,g,b,amt,p,f_name,l_name)
        print("errr")
        print("batch_id",b)
        User.objects.create(first_name=f_name,last_name=l_name,age=a,email=e,contact_number=cn,gender=g, batch_id=b)
        print("user create")
        obj=User.objects.filter(email=e)[0]
        u_id=obj
        Payment.objects.create(user_id=u_id,amount=amt,payment_successful=p)
        print("payrmrnt done")
        url_test = 'http://localhost:8000/completePayment'
        send_mail('Yoga For Life - Payment Link',
        'Dear '+f_name+',\n\nThanks for enrolling in our yoga class.\nCharges: Rs 500/month\nKindly make the payment with the link given below. You can make the payment within 30 days of enrolment to confirm your admission.\n\nLink:'+url_test+'\n\nThank you and see you soon:)\n\nBest,\nVartika',
        'fakeg9450@gmail.com',[e],fail_silently=True)
        print("mail sent")
        # subject = 'welcome to GFG world'
        # message = f'Hi , thank you for registering in geeksforgeeks.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['fakeg9450@gmail.com']
        # send_mail( subject, message, email_from, recipient_list )
        if(p=='True'):
            o=Payment.objects.filter(user_id=u_id)[0]
            p_id=o
            Admission.objects.create(payment_id=p_id,user_id=u_id,batch_id=b)
            print("Adminsiion create")
            

class UpdateSerializer(serializers.Serializer):
    email=serializers.EmailField()
    batch_id=serializers.IntegerField()
    print(batch_id)
    payment_successful=serializers.BooleanField()

    def save(self):
        e=self.get('email')
        b=self.get('batch_id')
        p=self.get('payment_successful')
        amt=self.get('amount')
        print('update done')
        User.objects.filter(email=e).update(batch_id=b)
        obj=User.objects.filter(email=e)[0]   
        u_id=obj
        Payment.objects.create(user_id=u_id,amount=amt,payment_successful=p)
        url_test = 'http://localhost:8000/payment'
    #     send_mail('Yoga For Life - Payment Link',
    #    'Hey,\n\nThanks for enrolling in our yoga class once again.\nCharges: Rs 500/month\nKindly make the payment with the link given below. You can make the payment within 30 days of enrolment to confirm your admission.\n\nLink: '+url_test+'\n\nThank you and see you soon:)\n\nBest,\nSanya',
    #     'fakeg9450@gmail.com',[e],fail_silently=True)
        # server.login('fakeg9450@gmail.com','V9450328091S')
        # server.sendmail('fakeg9450@gmail.com',e);
        # print('Mil sent')

        if(p=='True'):
            o=Payment.objects.filter(user_id=u_id)[0]
            p_id=o
            Admission.objects.create(payment_id=p_id,user_id=u_id,batch_id=b)
            print('update done')
            
