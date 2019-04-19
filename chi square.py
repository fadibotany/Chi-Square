def chi_square():
    number_of_phenotypes = int(input("How many different phenotypes do you have(NUMBER)? "))
    list_of_phenotypes = []
    list_of_observed = []
    list_of_expected = []
    list_of_total = []
    n = 0
    m = 0
    sum_total = 0
    total = 0
    
    for i in range(number_of_phenotypes):
        a = input('Enter the PHENOTYPE one at a time, then click enter: ')
        list_of_phenotypes.append(a)
    
    for i in range(len(list_of_phenotypes)):
        phenotype_observed = int(input('What was your OBSERVED for the ' + list_of_phenotypes[n] + " phenotype? " ))
        list_of_observed.append(phenotype_observed)
        n += 1
        total += phenotype_observed # get the total of the population
        
    expected_y_n= input('Do you Know the expected(yes/no)? ')
    
    if expected_y_n == "yes" or expected_y_n == " yes":
        n = 0
        for i in range(number_of_phenotypes):
            b = int(input('what is the expected for the ' + list_of_phenotypes[m] + ' phenotype? '))
            print('')
            list_of_expected.append(b)
            m += 1
        for i in list_of_phenotypes:
            c = float(((list_of_observed[n]- list_of_expected[n])**2)/float(list_of_expected[n]))
            list_of_total.append(c)
            if n == 0:
                print("Phenotype ------ observed -------- expected ------- Total")
                print('')
            print(list_of_phenotypes[n] + " ----- " +  str(list_of_observed[n]) + " ----- " + str(list_of_expected[n]) + " ----- " + str(list_of_total[n]))
            print("-----------------------------------------------------------")
            n += 1
            sum_total +=  c
        
        
        if len(list_of_phenotypes)-1 == 1: #finds degrees of freedom and the number of probability on the chart
            number = 3.84 
        if len(list_of_phenotypes)-1 == 2:
            number = 5.99
        if len(list_of_phenotypes)-1 == 3:
            number = 7.81
        if len(list_of_phenotypes)-1 == 4:
            number = 9.49 
            
        if sum_total < number:
            print('')
            print('CORRECT because total is less than the 5% probability value')
            print(str(sum_total) + ' < ' + str(number))
        elif sum_total > number:
            print('')
            print('NOT CORRECT because total is less than the 5% probability value')
            print(str(sum_total) + ' > ' + str(number))
            
          
    
            
    if expected_y_n == "no" or expected_y_n == " no":      
          
        ratio_y_n = input('do you know the ratio? (yes/no) ')
     
        if ratio_y_n == 'yes':
            ratio = input('what is the ratio (use colons to seperate the numbers)? ')
        if ratio_y_n == "no":
            print('Sorry, find the ratio first')
  
        if ratio == "9:3:3:1":
            f = (float(total * 9)/16)
            g = (float(total * 3)/16)
            h = (float(total * 3)/16)
            i = (float(total * 1)/16)
            list_of_expected.append(f)
            list_of_expected.append(g)
            list_of_expected.append(h)
            list_of_expected.append(i)

        
        if ratio == "1:1:1:1": 
            f = total * 0.25
            g = total * 0.25
            h = total * 0.25
            i = total * 0.25
            list_of_expected.append(f)
            list_of_expected.append(g)
            list_of_expected.append(h)
            list_of_expected.append(i)
            
        n = 0
        for i in list_of_phenotypes:          
            c = float(((list_of_observed[n]- list_of_expected[n])**2)/float(list_of_expected[n]))
            list_of_total.append(c)
            if n == 0:
                print("Phenotype ------ observed -------- expected ------- Total")
                print('')
            print(list_of_phenotypes[n] + " ----- " +  str(list_of_observed[n]) + " ----- " + str(list_of_expected[n]) + " ----- " + str(list_of_total[n]))
            print("-----------------------------------------------------------")
            n += 1
            sum_total +=  c
        
            
            
            
        if len(list_of_phenotypes)-1 == 1: #finds degrees of freedom and the number of probability on the chart
            number = 3.84 
        if len(list_of_phenotypes)-1 == 2:
            number = 5.99
        if len(list_of_phenotypes)-1 == 3:
            number = 7.81
        if len(list_of_phenotypes)-1 == 4:
            number = 9.49 
            
        if sum_total < number:
            print('')
            print('CORRECT because total is less than the 5% probability value')
            print(str(sum_total) + ' < ' + str(number))
        elif sum_total > number:
            print('')
            print('NOT CORRECT because total is less than the 5% probability value')
            print(str(sum_total) + ' > ' + str(number))


chi_square()     