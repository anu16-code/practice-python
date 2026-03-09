emoji_dict = {"happy": "😊"
              , "sad": "😔",
              "angry": "😠"
            }
text = input("Enter mood(happy, sad, angry):").lower()
if text in emoji_dict:
    print(emoji_dict[text])
else:
 print("mood not found")

