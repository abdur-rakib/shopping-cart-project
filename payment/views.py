import braintree
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from django.core.mail import send_mail

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    sent = False
    if request.method == 'POST':
        # Retrive nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # Create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the orderas paid
            order.paid = True
            # Store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            subject = 'Your order has been successfully placed'
            message = 'Name: {} {} \n Order ID: {}\nFor further query please call at 01767584854' .format(order.first_name, order.last_name,order.id)
            send_mail(subject, message, 'abdurrakib961@gmail.com', (order.email,))
            sent = True
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token:
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order, 'client_token': client_token}
                      )


def payment_done(request):
    return render(request,
                  'payment/done.html'
                  )


def payment_canceled(request):
    return render(request,
                  'payment/canceled.html'
                  )
