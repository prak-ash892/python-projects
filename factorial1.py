basic=int(input('enter basic salary:'))
if(basic>=4000):
    da=0.32*basic
    hra=0.15*basic
    cca=325
    net_salary=basic+da+hra+cca
    print('da:',da)
    print('hra:',hra)
    print('net salary is:',net_salary)
