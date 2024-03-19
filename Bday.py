from PIL import Image
import streamlit as st

#---- Assets ----
Alexis = Image.open("Images/alexis.jpg")

# Find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Happy Birthday", page_icon=':white_heart:', layout='wide')

# ---- HEADER ----

st.header("It's your special day today :two_hearts:")
st.title("Happiest 16th Birthday Alexissss<3")
left_column, right_column = st.columns((1, 2))
with left_column:
    st.image(Alexis)
with right_column:
    st.subheader("Today on March 20 you are now officially 16, a huge leap into your "
                 "life as one chapter closes and "
             "another is opened. I wish you the happiest day today miss ganda, "
                 "all of us are here for you today, "
             "tomorrow, and forever:33🎉😛🤗🥰😍🤪🎉")


# ---- Your Favorites ----
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Things That Alexis Likes')
        st.subheader(" Favourite Colours: Blue and Purple💜💙")
        st.subheader(" Favourite Foods: Fried Noodles, Fries(or any kind of cook in a potato🙌🙌)")
        st.subheader(" Favourite Fruits: Mango, Buko🍎🍎")
        st.subheader(" Favourite Drink: Okinawa🥤🥤")
        st.subheader(" Favourite Donut: Choco Butternut🥯🥯")
        st.subheader(" Favourite Cake: Mocha, Mango🎂🎂")
        st.subheader(" Favourite Dish: Chicken Curry🍖🍗")
        st.subheader(" Favourite Flower: Tulips🌷🌷🌷")


#---- Pictures ----
with st.container():
    st.write("---")
    st.title("Blehhhh,,, Messages from ur BBs")
    st.subheader("From Clara💋💖(si bading)")
    st.write("O my beautiful and loving babygirl Alexis,3 YEARS NA PALA TAYO MAGKAKILALA NOH parang naaalala ko nung "
             "una palang tayo nagkita nung reading camp,maliit na babaeng ibubuhat sa cheerleading pa yung tawag ko sayo nun. "
             "Naaalala ko nung mga times na sobra sobra sobranggg daldal mo sa chat tapos nabubuhayan ka everytime may chika ako"
             " tunkol kay edlhyn😭. Tapos pagnagkikita tayo sa school apaka akward pa ng interaction natin nun, pero g na g tayo pag nagcocover "
             "ng kpop group dances sa stage! Siguro thank you din kay Angel kasi kung di kayo naging magkaclassmate noon,"
             "nagkalimutan na tayo, chaka nagkachance pa tayo ulit nung nasama kita doon sa first dance contest ko with"
             "you nung Christmas hihi...")
    st.write("##")
    st.write("Ngayon, I'm very thankful kasi nabalik ulit yung spark natin together pero mas very strong na..."
             " I'm so thankful na I got to keep you in my life ngayon as one of the most important people na that "
             "I have ever met. I know in the future baka iba ibang landas na yung mapuntahan natin pero remember na "
             "I'll always find a way para mag reunite ulit tayo, because promise ko talaga we'll both be successful babygirls in the future."
             " Happy 16th birthday my baby and always remember na we're here lang for you!!! Enjoy your birthday and your brand new year to live in!♥️"
             " Neomu saranghae I loveyou so much")
    st.write("##")
    st.write("##")
    st.header("From Angel💕😊👌")
    st.write("Hi Alex 😔☝️ Happy 16th birthday, my love!!! I hope you'll surround yourself with positive people so that you won't deal with something "
             "that is harmful for your mental health (tas biglang kasama ako sa na-block😠) May your heart always be in peace and when you feel "
             "troubled you can always run to me. I promise that I'll listen and cry with you🥺🥺 Ako na to oh🧍🧍 And if dumating yung time na ready"
             " to love ka na, I'll support you kahit sino pa yan as long as you're happy. Bibigwasan ko yan pag pinaiyak ka.")


 #---- A message from me to you----
st.write("---")
st.title("A Message from Me😝😝😝")
st.write("##")
st.header("From Me to You💕🤗")
st.write("  Hi Alexissssss Happiest 16th and kay maam aloha(joke lang po). It's been months na since we've been classmates and recently mas napapalapit "
         "ako sa circle mo(ang kulit kasi ni clara) pero im very happy i got to know you guys and i hope i get to know you more:), I never would have "
         "thought na I'll be able to get close with you guys(nung inaasar asar ko kayo kasi nagcocover kayo ng dance sa library bwhahahaha) pero I'm very "
         "thankful that i did since you guys are super fun to be with. I can tell na you guys really love each other specially you, you've been nothing but "
         "kind to everyone and i really love that. Thank you for everything, you have shown me how friends should treat each other, with love, and respect, and " 
         "to overall just have fun with them.")










