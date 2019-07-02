##this is an example of string functions
s=str(input("enter any string: "));
##manipulation functions
#a=str(input("enter character u want to count/find:"));
#c=s.count(a);
#print(c);

#c=s.find(a);
#print(c);

#r=s.replace('n',a);
#print(r);
#p=s.split('#');
#print(p)


#c=s.upper();
#print(c);


#t=s.title();
#print("title wise:%s" %t);


#t=s.capitalize();
#print("capitalize:"+t);


#t=s.swapcase();
#print(t);

#t=s.strip('@');
#print("after strip:"+t);
#t=s.lstrip('!' '#' '@' '$' '%' '&' '*');
#print("after left strip:"+t);
#t=s.rstrip('!' '#' '@' '$' '%' '&' '*');
#print("after right strip:"+t);

#t=s.ljust(50);
#print("after ljust:"+t);
#t=s.rjust(50);
#print("after rjust:"+t);
#t=s.center(50);
#print("after center:"+t);

t='+';
print(t.join(s));
##test funtions
#a=s.isupper();
#print(a);

#a=s.isdigit();
#print(a);

#a=s.endswith("#");
#a=s.isspace();
a=s.istitle();
print(a);
