from py2 import list_example
while True:
    print("****************************__LAB EXERCISE 2__****************************")
    print("\n 1 ->  List ")
    print("\n 2 ->  Dictionaries")
    print("\n 3 -> Exit.")
    print("**************************************************************************")
    choice = int(input("\n\nEnter your choice : "))
    if (choice == 1):   
          my_list = []
          my_list.append("01")          
          my_list.append("arigato")              
          my_list.append("Computer Science")               
          my_list.append("MCA")  
          my_list.append("8.5 GPA")             
          my_list.append("8417962000")        
          my_list.append("90%")                 
          my_list.append("anshbhandari.13@gmail.com")
          my_list.append("Male") 

          print("List:", my_list)

 
          my_list.insert(1, "Ansh Bhandari") 
          my_list.insert(7, "HOD") 
    
          print("List:", my_list)

          dic = {
          'address': '2nd Cross S.G Palya',
          'city': 'Bangalore',
          'zipcode': '560029'
         }
    
          my_list.extend(['INDIA', 'User']) 
          my_list.extend(list(dic.keys())) 

          print("List:", my_list)

          if __name__ == "__main__":
           list_example()
        
          my_list = [132, 22, 863, 426, 519]

          first_element = my_list[0]
          last_element = my_list[-1]
          my_list[0] = last_element
          my_list[-1] = first_element
          print(my_list)


          def sum_of_digits(list_of_numbers):
            sum_of_digits = 0
            for number in list_of_numbers:
                sum_of_digits += number
                return sum_of_digits
            print(sum_of_digits(my_list))


          def smallest_element(list_of_numbers):
            smallest_element = list_of_numbers[0]
            for number in list_of_numbers:
                if number < smallest_element:
                 smallest_element = number
                 return smallest_element

            print(smallest_element(my_list))
            
# Sort the dictionaries in ascending order based on the Key of the dictionary.
#  Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary.
#  Write a Python code to demonstrate the sorting in descending order of values with lambda function

    elif (choice == 2):
        my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
        print("Dictionary sorted in ascending order based on keys:", sorted_dict)


        my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        sum_of_values = sum(my_dict.values())
        print(" Sum of all values in the dictionary:", sum_of_values)



        my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        sorted_dict_descending = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        print("Descending Order :",sorted_dict_descending)
        
    elif choice == 3:
        break
    else:
        print("\nInvalid Input : Please try again")