import streamlit as st
from streamlit_option_menu import option_menu

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
                },
    'Add-Ons': {
                'Nail Art': {
                            'Per Nail':['$5+','5+ mins'],
                            'Full Set' :['$25+','30+ mins']
                            },
                'Gel Polish': {
                            'Gel Polish':['$15+','15+ mins']
                            },
                'Nail Repair': {
                            'Nail Repair':['$10+','5+ mins']
                            },
                'Nail Removal': {
                            'Nail Removal':['$20','15+ mins']
                            }
            },
    'Waxing': {
                'Eyebrows': {
                    'Eyebrows':['$12','15+ mins']
                    },
                'Chin': {
                    'Whole Chin':['$20','10+ mins']
                    },
                'Lip': {
                    'Lip':['$10','10+ mins']
                    },
                'Face': {
                    'Whole Face':['$40','20+ mins']
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


#`---Add-Ons---`
def add_ons_services ():
    for sub_service, enhance in all_services['Add-Ons'].items():
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

#`---Waxing---`
def waxing():
    for sub_service, enhance in all_services['Waxing'].items():
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

def option_menus():
    with st.sidebar:
        selected = option_menu(menu_title=None,
                               options= ['Services', 'Drinks'],
                               icons=['book', 'water'],
                               default_index=0)
        
    if selected == 'Services':
        main()
    elif selected == 'Drinks':
        drink_menu()
 
def main():
    # ---Title and Header---
    st.markdown(
        """
        <div class="box">
        <h1>Welcome to Alo Nail Lounge</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    basic_services,enhance,add_ons,wax = st.tabs(["Mani & Pedi", "Nail Enhancement","Add-Ons","Waxing"])
    
    with basic_services:
        basic()
    with enhance:
        nail_enhancement()
    with add_ons:
        add_ons_services()
    with wax:
        waxing()

def drink_menu():
    st.title("Drink Menu")
# Embed CSS in the app
    st.markdown(
        """
        <style>
            .drink-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                gap: 20px;
                border-radius: 12px;
            }
            .drink-item {
                flex: 0 0 30%; /* Each item takes up 30% of the row */
                text-align: left;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                background-color: #f9f9f9;
                border-radius: 10px;
            }
            .drink-item h3 {
                margin: 10px 0;
                font-size: 32px;
                color: #333;
            }
            .row-divider {
                width: 100%;
                border-top: 1px solid #ddd;
                margin: 20px 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sample drink data
    menu = {
            'Drink' : ["Coffee", "Tea", "Diet/Classic", "Water","Sprite"],
            'Ahcoholic' : ["Red Wine","White Wine", "Beer", "Bellini", "Mimosas",'Charmpagne']
    }

    # HTML container for the drink items
    st.markdown('<div class="drink-container">', unsafe_allow_html=True)


    # Display the drinks
    for category, drinks in menu.items():
        st.write(f'<h2 class="box">{category}</h2>', unsafe_allow_html=True)
        for drink in drinks:
            st.markdown(
                f"""
                <div class="drink-item">
                    <h3>{drink}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )
        st.markdown('<div class="row-divider"></div>', unsafe_allow_html=True)
            

# Close the container
st.markdown('</div>', unsafe_allow_html=True)

    
if __name__ == '__main__':
   option_menus()    