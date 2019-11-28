def entry(String val):
    if val in user_tags:
        servo_motor()
def billcalc(String val):
    if val not in d:
        return True
    elif val in d:
        cost=0
        for k,v in d.items():
            for k1,v1 in v.items():
		cursor.execute("SELECT ITEM_COST FROM ITEM_LIST WHERE ITEM_ID=?",(k1))
                r=cursor.fetchone()
                cost+=r*v1
        cursor.execute("SELECT BALANCE FROM CUSTOMER WHERE CUS_ID=?",(val))
        rr=cursor.fetchone()
        if(cost<=rr):
            return True
    else:
        return False
def exit(String val):
    if val in user_tags:
        a=billcalc(val)
        if(a==True):
            servo_motor()
            del d[val]
        else:
            print("insufficient balance")

        
    
