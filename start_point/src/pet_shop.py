# # WRITE YOUR FUNCTIONS HERE
# def test_pet_shop_name(self):
#         name = get_pet_shop_name(self.cc_pet_shop)
#         self.assertEqual("Camelot of Pets", name)
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#     @unittest.skip("delete this line to run the test")
#     def test_total_cash(self):
#         sum = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1000, sum)
def get_total_cash(pet_shop_finances):
    return pet_shop_finances["admin"]["total_cash"]

#     @unittest.skip("delete this line to run the test")
#     def test_add_or_remove_cash__add(self):
#         add_or_remove_cash(self.cc_pet_shop,10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)

#     @unittest.skip("delete this line to run the test")
#     def test_add_or_remove_cash__remove(self):
#         add_or_remove_cash(self.cc_pet_shop,-10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(990, cash)
def add_or_remove_cash(pet_shop, cash_value):
    new_cash_total = get_total_cash(pet_shop) + cash_value
    pet_shop["admin"]["total_cash"] = new_cash_total

# @unittest.skip("delete this line to run the test")
#     def test_pets_sold(self):
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(0, sold)
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#     @unittest.skip("delete this line to run the test")
#     def test_increase_pets_sold(self):
#         increase_pets_sold(self.cc_pet_shop,2)
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(2, sold)
def increase_pets_sold(pet_shop, number_of_pets_sold):
    total_pets_sold = get_pets_sold(pet_shop) + number_of_pets_sold
    pet_shop["admin"]["pets_sold"] = total_pets_sold

#     @unittest.skip("delete this line to run the test")
#     def test_stock_count(self):
#         count = get_stock_count(self.cc_pet_shop)
#         self.assertEqual(6, count)
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#     @unittest.skip("delete this line to run the test")
#     def test_all_pets_by_breed__found(self):
#         pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
#         self.assertEqual(2, len(pets))

# @unittest.skip("delete this line to run the test")
#     def test_all_pets_by_breed__not_found(self):
#         pets = get_pets_by_breed(self.cc_pet_shop, "Dalmation")
#         self.assertEqual(0, len(pets))
def get_pets_by_breed(pet_shop, breed):
    pets_by_breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed_list.append(pet["breed"])
    
    return pets_by_breed_list

#     @unittest.skip("delete this line to run the test")
#     def test_find_pet_by_name__returns_pet(self):
#         pet = find_pet_by_name(self.cc_pet_shop, "Arthur")
#         self.assertEqual("Arthur", pet["name"])

#     @unittest.skip("delete this line to run the test")
#     def test_find_pet_by_name__returns_None(self):
#         pet = find_pet_by_name(self.cc_pet_shop, "Fred")
#         self.assertIsNone(pet)
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# @unittest.skip("delete this line to run the test")
#     def test_remove_pet_by_name(self):
#         remove_pet_by_name(self.cc_pet_shop, "Arthur")
#         pet = find_pet_by_name(self.cc_pet_shop,"Arthur")
#         self.assertIsNone(pet)
def remove_pet_by_name(pet_shop, pet_name):
    eliminated_pet = find_pet_by_name(pet_shop, pet_name)
    # print(pet_shop["pets"])
    pet_shop["pets"].remove(eliminated_pet)
    # print("                                    ")
    # print(pet_shop["pets"])

#     @unittest.skip("delete this line to run the test")
#     def test_add_pet_to_stock(self):
#         add_pet_to_stock(self.cc_pet_shop, self.new_pet)
#         count = get_stock_count(self.cc_pet_shop)
#         self.assertEqual(7, count)
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

#     @unittest.skip("delete this line to run the test")
#     def test_customer_cash(self):
#         cash = get_customer_cash(self.customers[0])
#         self.assertEqual(1000, cash)
def get_customer_cash(paying_customer):
    return paying_customer["cash"]

#     @unittest.skip("delete this line to run the test")
#     def test_remove_customer_cash(self):
#         customer = self.customers[0]
#         remove_customer_cash(customer, 100)
#         self.assertEqual(900, customer["cash"])
def remove_customer_cash(paying_customer, payment_amount):
    updated_blanace = get_customer_cash(paying_customer) - payment_amount
    paying_customer["cash"] = updated_blanace

# @unittest.skip("delete this line to run the test")
#     def test_customer_pet_count(self):
#         count = get_customer_pet_count(self.customers[0])
#         self.assertEqual(0, count)
def get_customer_pet_count(customer):
    return len(customer["pets"])

#     @unittest.skip("delete this line to run the test")
#     def test_add_pet_to_customer(self):
#         customer = self.customers[0]
#         add_pet_to_customer(customer, self.new_pet)
#         self.assertEqual(1, get_customer_pet_count(customer))
def add_pet_to_customer(new_owner, pet):
    new_owner["pets"].append(pet)

    # --- OPTIONAL ---

    # @unittest.skip("delete this line to run the test")
    # def test_customer_can_afford_pet__sufficient_funds(self):
    #     customer = self.customers[0]
    #     can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
    #     self.assertEqual(True, can_buy_pet)

    # @unittest.skip("delete this line to run the test")
    # def test_customer_can_afford_pet__insufficient_funds(self):
    #     customer = self.customers[1]
    #     can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
    #     self.assertEqual(False, can_buy_pet)

    # @unittest.skip("delete this line to run the test")
    # def test_customer_can_afford_pet__exact_funds(self):
    #     customer = self.customers[2]
    #     can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
    #     self.assertEqual(True, can_buy_pet)
def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else: return False

    # These are 'integration' tests so we want multiple asserts.
    # If one fails the entire test should fail
    #
    # @unittest.skip("delete this line to run the test")
    # def test_sell_pet_to_customer__pet_found(self):
    #     customer = self.customers[0]
    #     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

    #     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    #     self.assertEqual(1, get_customer_pet_count(customer))
    #     self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
    #     self.assertEqual(100, get_customer_cash(customer))
    #     self.assertEqual(1900, get_total_cash(self.cc_pet_shop))
def get_pet_cost(pet_shop, pet):
    # return pet["price"]
    if find_pet_by_name(pet_shop, pet["name"]) == None:
        print(find_pet_by_name(pet_shop, pet))
        return 0
    else: return pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    # pet_cost = pet["price"]
    original_stock = get_stock_count(pet_shop)
    pet_cost = get_pet_cost(pet_shop, pet)
    # print(pet_cost)

    add_pet_to_customer(customer, pet)
    remove_pet_by_name(pet_shop, pet["name"])
    increase_pets_sold(pet_shop, (original_stock - get_stock_count(pet_shop)))
    remove_customer_cash(customer, pet_cost)
    add_or_remove_cash(pet_shop, pet_cost)

    # @unittest.skip("delete this line to run the test")
    # def test_sell_pet_to_customer__pet_not_found(self):
    #     customer = self.customers[0]
    #     pet = find_pet_by_name(self.cc_pet_shop,"Dave")

    #     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    #     self.assertEqual(0, get_customer_pet_count(customer))
    #     self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
    #     self.assertEqual(1000, get_customer_cash(customer))
    #     self.assertEqual(1000, get_total_cash(self.cc_pet_shop))

    #     @unittest.skip("delete this line to run the test")
    # def test_sell_pet_to_customer__insufficient_funds(self):
    #     customer = self.customers[1]
    #     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

    #     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    #     self.assertEqual(0, get_customer_pet_count(customer))
    #     self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
    #     self.assertEqual(50, get_customer_cash(customer))
    #     self.assertEqual(1000, get_total_cash(self.cc_pet_shop))