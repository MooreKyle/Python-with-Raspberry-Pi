#dictionary_remove_item.py

def main():
    dry_goods_dict = {"flour":4.99,"beans":3.27,"rice":6.78}
    for dry_good,price in dry_goods_dict.items():
        print(dry_good + "costs " + format(price,".2f"))
    item_str = input("Enter a dry good to remove ")
    while (item_str != "exit") and (len(dry_goods_dict) > 0):
        try:
            #del(dry_goods_dict[item_str])
            price = dry_goods_dict.pop(item_str)
            print("item removed price = {0:.2f}".format(price))
        except KeyError:
            print(item_str + " not removed")
        print(dry_goods_dict)
        #print(len(dry_goods_dict))
        if len(dry_goods_dict) > 0:
            item_str = input("Enter a dry good to remove ")
    dry_goods_dict.clear() # remove all items
    print(dry_goods_dict)
        
main()
