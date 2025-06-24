my_list=[5,2,9,1]
my_tuple=(10,20,30)
my_set={6,3,9}
my_dict={'a':1,'b':2}
while True:
    print("\n Choose a data type to operate on:")
    print("1.List")
    print("2.Tuple")
    print("3.Set")
    print("4.Dictionary")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        print("\n List Operations\n")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Sort")
        print("6.Search")
        op=input("Enter operation:")
        if op=='1':
            val=int(input("Enter value to insert:"))
            my_list.append(val)

        elif op=='2':
            i=int(input("Enter index:"))
            val=int(input("Enter val:"))
            if 0<=i<len(my_list):
                my_list[i]=val
          
        elif op=='3':
            val=int(input("Enter val to delete:"))
            if val in my_list:
                my_list.remove(val)
                
        elif op=='4':
            print("List:",my_list)
            
        elif op=='5':
            my_list.sort()
            print("Sorted List:",my_list)
            
        elif op=='6':
            val=int(input("Enter val to search:"))
            print("Found!" if val in my_list else "Not Found")
            
    elif choice=='2':
        print("Tuple(immutable)-only display/search allowed")
        print("Tuple:",my_tuple)
        val=int(input("Enter val to search:"))
        print("Found!" if val in my_tuple else "Not Found")
        
    elif choice=='3':
        print("\n Set operations:\n")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Sort")
        print("6.Search")
        op=input("Enter operation:")
        if op=='1':
            val=int(input("Enter val to add:"))
            my_set.add(val)
        elif op=='2':
            vald=int(input("Enter val to delete:"))
            val=int(input("enter val to update:"))
            my_set.discard(vald)
            my_set.add(val)
        elif op=='3':
            val=int(input("Enter val to discard:"))
            my_set.discard(val)
        elif op=='4':
            print("Set:",my_set)
        elif op=='5':
            sorted_s=sorted(my_set)
            print("Sorted List:",sorted_s)
        elif op=='6':
            val=int(input("Enter val to search:"))
            print("Found!" if val in my_set else "Not found!")
            
    elif choice=='4':
        print("\n Dictionary Operations\n")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Search")
        print("6.Sort")
        op=input("Enter operation:")
        
        if op=='1':
            key=input("Enter key:")
            val=int(input("Enter val:"))
            my_dict[key]=val
            print(my_dict)
        elif op=='2':
            key=input("Enter key:")
            val=int(input("Enter val:"))
            my_dict[key]=val
        elif op=='3':
            key=input("Enter key:")
            my_dict.pop(key,None)
        elif op=='4':
            print("Dictionary:",my_dict)
        elif op=='5':
            key=input("Enter key to search:")
            print("Found!" if key in my_dict else "Not found")
        elif op=='6':
            print("Ordered by default")
    elif choice=='5':
        print("Exiting program")
        break
    else:
        print("Invalid choice,try again.")
