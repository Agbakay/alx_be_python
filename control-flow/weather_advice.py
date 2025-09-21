weather = input("What;s the weather like today? (sunny, rainny, cold)")
if weather == 'sunny':
    print("Wear a t-shirt and sunglasses")
    if weather == 'rainny':
        print("Don't forget your umbrella and a raincoat")
        if weather == 'cold':
            print(" Sorry, I don't have recommendations for this weather.")
    else:
        print(" Sorry, I don't have recommendations for this weather.")