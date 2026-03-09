"""
Адаптер оборачивает несовместимый объект и делает его совместимым с нужным интерфейсом.

"""

class NewPayment:
    def pay(self, amount):
        return f"{amount} was payed via new payment system"

class OldPayment:
    def make_payment(self, rubles):
        return f"The payment of {rubles} rubles was made"

class PaymentAdapter:
    def __init__(self, old_system):
        self.old = old_system

    def pay(self, amount):
        rubles = amount * 85
        return self.old.make_payment(rubles)

def process_payment(payment_system, amount):
    print(f"{payment_system.pay(amount)}")

amount = 100

new_system = NewPayment()
process_payment(new_system, amount)

old_system = OldPayment()
adapter = PaymentAdapter(old_system)
process_payment(adapter, amount)

