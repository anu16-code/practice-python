mood_dict ={"😊":"happy",
            "😔":"sad"
            ,"😠":"angry",
            "❤️":"love"
            }
emoji = input("Write an emoji(😊,😔,❤️,😠)")
if emoji in mood_dict:
    print("mood is", mood_dict[emoji])
else:
    print("can not find mood")
