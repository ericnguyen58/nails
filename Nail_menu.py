import streamlit as st

def style(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


style("style.css")
# ---Title and Header---
st.markdown("<h1 style='text-align: center'>Welcome to Alo Nail Lounge</h1>",unsafe_allow_html=True)

#`---Manicure---`
def manicure():
    
    categories = {'Basic Manicure':['$20','30 mins'],
                  'Alo Manicure' :['$45','45 mins'],
                  'Gel Polish':['$15','10-15 mins extra']}
    for service in categories:
        st.write(f"""
            <div class="service-container">
                <h3>{service}</h3>
                <h3>{categories[service][0]}</h3>
            </div>
            <p class="service-duration">{categories[service][1]}</p>
        """, unsafe_allow_html=True)
        st.write("<hr>", unsafe_allow_html=True)
    
    
#`---Pedicure---`
def pedicure():
    categories = {'Basic Pedicure':['$35','30 mins'],
                  'Pamper Pedicure' :['$55','45 mins'],
                  'Alo Pedicure' :['$75','60 mins'],
                  'Gel Polish':['$15','10-15 mins extra']}
    for service in categories:
        st.write(f"""
            <div class="service-container">
                <h3>{service}</h3>
                <h3>{categories[service][0]}</h3>
            </div>
            <p class="service-duration">{categories[service][1]}</p>
        """, unsafe_allow_html=True)
        st.write("<hr>", unsafe_allow_html=True)

#`---Nail Enhancement---`
def nail_enhancement():

    selected_services = st.multiselect(
    'Select a service',
    ['Full Set', 'Fill', 'Gel-X', 'Dip Powder/SNS', 'Silk Wrap']
)
    categories = {
        'Full Set':{
            "Acrylic":['$45','1 hr'],
            "Hard Gel":['$75','90 mins'],
            "Lumiary":['$60','1 hr']
                              },
                  
        'Fill':{
            "Acrylic":['$30','45 mins'],
            "Hard Gel":['$50','1 hr'],
            "Lumiary":['$50','1 hr']},
                    
        'Gel-X':{
            "Gel-X":['$65','1 hr']
            },
        'Dip Powder/SNS':{
            "Dip Powder/SNS":['$45','1 hr']
            },
        'Silk Wrap':{
            "Fiberglass Overlay":['$60','1 hr'],
            "Fiberglass Fill":['$40','1 hr']
            }
        }
    for service in categories:
        if service in selected_services:
            st.write(f"<h3 style='text-align: center'>~~{service}~~</h3>", unsafe_allow_html=True)
            for sub_service, details in categories[service].items():
                st.write(f"""
                    <div class="service-container">
                        <h3>{sub_service}</h3>
                        <h3>{details[0]}</h3>
                    </div>
                    <p class="service-duration">{details[1]}</p>
                """, unsafe_allow_html=True)
                st.write("<hr>", unsafe_allow_html=True)


if __name__ == '__main__':
    # image_path = 'logo.avif'
    # st.image(image_path)
    mani,pedi,enhance = st.tabs(["Manicure", "Pedicure", "Nail Enhancement"])
    with mani:
        manicure()
    with pedi:
        pedicure()
    with enhance:
        nail_enhancement()

    