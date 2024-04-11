import random
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
def send_otp(to_email):
    otp = random.randint(1111,9999)
    subject = 'Your Message'
    message = f"""
    Dear 'username',
    OTP: {otp}
   
    """
    
    from_email = settings.EMAIL_HOST_USER
    
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email,])
            print('mail send successfully')
            return {'status':'200','message':'otp send successfully...','otp':otp,}
        except BadHeaderError:
            return {'status':'500','message':'Failed to send otp...',}
        
    else:    
        return {'status':'400','message':'Invalid email address....Please reenter email!',}
    
def send_mail(user,to_email,msg):
    print('sending mail')
    subject = f'Contanct from {user}'
    message = f"""{msg}
    """
    
    from_email = settings.EMAIL_HOST_USER
    print(from_email)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email,])
            print('mail send successfully')
            return {'status':'200','message':'mail send successfully...'}
        except BadHeaderError:
            return {'status':'500','message':'Failed to send otp...',}
        
    else:  
        print('invalid')  
        return {'status':'400','message':'Invalid email address....Please reenter email!',}