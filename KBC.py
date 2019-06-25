question_list=["virat kohli ki wife a naam kya hai?",
                "salman khan ki sister ka naam kya hai?",
                "navgurukul kaha hai?",
                "MP ki rajdhani kaha hai?"]
frist_options=["anushka","priya","ujjain","bhopal"]
second_options=["megha","deepika","banglore","dewas"]
third_options=["bindu","arpita","dharamshala","ujjain"]
fourth_options=["etrina","sonam","new-york","dehli"]
all_options=["frist_options","second_options","third_options","fourth_options"]
ans_key=[1,3,3,1]
life_line=["anushka","priya","banglore","bhopal"]
life_line1=["bindu","arpita","new-york","dewas"]    
i=0
index=0
len_list=len(question_list)
while i<len_list:
    print question_list[i]
    print frist_options[i]    
    print second_options[i]
    print third_options[i]
    print fourth_options[i]
    user_input1=int(raw_input("enter your answer////o you want to use life_line so can enter 5050//:-"))
    if index==1:
        print "you have no lifeline"
        print " "
        continue
    elif ans_key[i]==user_input1:
        print"your ans right" 
    elif 5050==user_input1:
        print life_line[i]
        print life_line1[i]
        user_input=input("enter your answer//")
        if ans_key[i]==user_input:
            print"your ans right"    
        else:
            print"your ans wrong"
	index=index+1
            
    i=i+1

