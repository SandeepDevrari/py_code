##this is an another example of dictionary
states={'uk':'uttarakhand','up':'uttar pradesh','hp':'himanchal pradesh'};
cities={'uk':'dehradun,chamoli','up':'moradabad,noida','hp':'shimla'};
for i in states:
    #print(i);
    for e in cities:
        if i==e:
            print(states[i]+"-"+cities[e]);
