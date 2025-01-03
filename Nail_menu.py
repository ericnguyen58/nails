import streamlit as st

def style(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F4FA; /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

style("style.css")
# ---Title and Header---
st.markdown(
    """
    <div class="box">
      <h1>Welcome to Alo Nail Lounge</h1>
    </div>
    """,
    unsafe_allow_html=True
)


all_services = {
    'Mani & Pedi': {
                'Manicure': {
                            'Basic Manicure':['$25+','30+ mins'],
                            'Alo Manicure' :['$45+','45+ mins']
                            },
                'Pedicure': {
                            'Basic Pedicure':['$35+','30 mins'],
                            'Pamper Pedicure' :['$55+','45 mins'],
                            'Alo Pedicure' :['$75+','60 mins'],
                            }
        },
    'Nail Enhancement': {
                'Full Set':{
                    "Acrylic":['$45+','1+ hr'],
                    "Hard Gel":['$75+','90+ mins'],
                    "Lumiary":['$60+','1+ hr']
                                    },
                        
                'Fill':{
                    "Acrylic":['$30+','45+ mins'],
                    "Hard Gel":['$50+','1+ hr'],
                    "Lumiary":['$50+','1+ hr']},
                            
                'Gel-X':{
                    "Gel-X":['$65+','1+ hr']
                    },
                'Dip Powder/SNS':{
                    "Dip Powder/SNS":['$45','1+ hr']
                    },
                'Silk Wrap':{
                    "Fiberglass Overlay":['$60+','1+ hr'],
                    "Fiberglass Fill":['$40+','1+ hr']
                    }
                }
    }   
#`---Manicure---` and `---Pedicure---`
def basic():
    for sub_service, enhance in all_services['Mani & Pedi'].items():
        st.write(f'<h2 class="box">{sub_service}</h2>', unsafe_allow_html=True)
        for service, detail in enhance.items():
            st.write("<hr>", unsafe_allow_html=True)
            st.write(f"""
                <div class="service-container">
                    <h3>{service}</h3>
                    <h3>{detail[0]}</h3>
                </div>
                <p class="service-duration">{detail[1]}</p>
            """, unsafe_allow_html=True)
            st.write("<hr>", unsafe_allow_html=True)

    


#`---Nail Enhancement---`
def nail_enhancement():
    st.write( '<h2 class="box">Nail Enhancement</h2>',unsafe_allow_html=True)
    selected_services = st.multiselect(
        'Select a service',
        ['Full Set', 'Fill', 'Gel-X', 'Dip Powder/SNS', 'Silk Wrap']
    )

    for sub_service, enhance in all_services['Nail Enhancement'].items():
        if sub_service in selected_services:
            st.write(f'<h2 class="box">{sub_service}</h2>', unsafe_allow_html=True)
            for service, detail in enhance.items():
                st.write("<hr>", unsafe_allow_html=True)
                st.write(f"""
                    <div class="service-container">
                        <h3>{service}</h3>
                        <h3>{detail[0]}</h3>
                    </div>
                    <p class="service-duration">{detail[1]}</p>
                """, unsafe_allow_html=True)
                st.write("<hr>", unsafe_allow_html=True)


if __name__ == '__main__':
    basic_services,enhance,add_ons = st.tabs(["Mani & Pedi", "Nail Enhancement","Add-Ons"])
    
    with basic_services:
        basic()
    with enhance:
        nail_enhancement()
        
    
        
    # drink = st.columns(2)
    # with drink[0]:
    #     st.write("### Beverages")
    #     st.write("Complimentary beverages are available")
        
    # with drink[1]:
    #     st.write("### Beverages")
    #     st.write("Complimentary beverages are available")
    # radio = st.radio("Would you like a drink?", ["Yes", "Yeahr"])