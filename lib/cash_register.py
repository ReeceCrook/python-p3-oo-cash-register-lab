#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0, total=0, items=None):
    items = []
    self.total = total
    self.items = items
    self.discount = discount
    self.last_price = 0

  def get_total(self):
    return self._total
  
  def set_total(self, total):
    self._total = total
  
  def get_discount(self):
    return self._discount
  
  def set_discount(self, discount):
    self._discount = discount
  
  def get_items(self):
    return self._items
  
  def set_items(self, items):
    self._items = items

  

  def add_item(self, title, price, quantity=1):
    for i in range(quantity):
      self.items.append(title)
    self.total += price * quantity
    self.last_price = price * quantity
    return self.items

  def apply_discount(self):
    if self.discount != 0:
      new_discount = self.total * (self.discount / 100)
      self.total -= new_discount
      print(f"After the discount, the total comes to ${ int(self.total) }.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_price
    return float(self.total)
    
  total = property(get_total, set_total)
  discount = property(get_discount, set_discount)
  items = property(get_items, set_items)

