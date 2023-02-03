#dictionary_define_functions.py

def sale_fun(original_dict:dict,discount:float)->dict:
    sale_dict = {}
    for key,value in original_dict.items():
        sale_dict[key] = value * (1 - discount/100)
    return sale_dict

def sale_fun_2(original_dict:dict,item_name:str,discount:float)->None:
    if item_name in original_dict:
        original_dict[item_name] = original_dict[item_name] \
                                   * (1 - discount/100)

def main():
    dry_goods_dict = {"beans":7.99,"rice":3.45,"flour":2.99}
    updated_dict = sale_fun(dry_goods_dict,10)
    for dry_good_name,dry_good_cost in dry_goods_dict.items():
        print(dry_good_name)
        print(dry_good_cost)
    for dry_good_name,dry_good_cost in updated_dict.items():
        print(dry_good_name)
        print(format(dry_good_cost,".2f"))
    help(sale_fun)
    discount_item = input("Enter the name of the item with the discount ")
    sale_fun_2(dry_goods_dict,discount_item,20)
    for dry_good_name,dry_good_cost in dry_goods_dict.items():
        print(dry_good_name)
        print(dry_good_cost)

main()
