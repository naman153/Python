def str_count(str):
    count1,count2,count3,count4=0,0,0,0
    vowel=set("aeiouAEIOU")
    digit=set("1234567890")
    for alphabet in str:
        if alphabet in vowel:
            count1=count1+1
        elif alphabet in " ":
            count3=count3+1
        elif alphabet in digit:
            count4=count4+1
        else:
            count2=count2+1
    print("No. of vowels.:",count1)
    print("No. of consonant:",count2)
    print("No. of white spaces:",count3) 
    print("No. of digits:",count4)
str1=input("Enter the string:")
str_count(str1)




