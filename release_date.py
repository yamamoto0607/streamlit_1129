import streamlit as st

st.title('ラーメン記録簿')
st.write('食べたラーメンを記録しておくアプリです。')
name= st.text_input('行ったお店の名前')
menu= st.text_input('頼んだラーメン')
price= float(st.number_input('価格（税込）') )
menn = st.selectbox('麺は？',list(['極太麵','太麺','中太麺','中細麵''細麵','極細麺']))
soup = st.selectbox('味は？',list(['醤油','味噌','塩','豚骨','白湯系','魚介系','油そば','その他']))
if soup =='その他':
    soup2= st.text_input('その他（書き込み）')
ingredients = st.multiselect('具材は？',
                             ['焼豚','鶏肉','海苔','ねぎ','白髪ねぎ','メンマ','ほうれん草','卵','キャベツ','もやし','ナルト','紅ショウガ','コーン','バター','高菜','その他']
                             )
comment= st.text_area('感想')
left_column,right_column = st.columns(2)
button= right_column.button('確定')




name2 = ('行ったお店は'+ name)
order = ( menu +'を頼んだ'+'('+ str(price)+'円)')
col1, col2 = st.columns(2)
if  button == True:
    col1.write('お店のデータ')
    col1.write( name2 )
    col1.write(order)
    col2.write('ラーメンのデータ')
    col2.write(menn)
    if soup=='その他':
        col2.write(soup2)
    else:
        col2.write(soup)
    col2.write(ingredients)
    st.write( comment )
    st.write('スクリーンショットで記録しましょう！')



st.title('明日も美味しいラーメンを探しましょう。')
