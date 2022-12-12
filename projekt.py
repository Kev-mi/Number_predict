import streamlit as st
import design.website as webdesign
import models.ml_models as models
import scraper.image_scraper as scraper


def main():
    st.set_page_config(layout="wide")
    sidebar_1_selected_option = st.sidebar.selectbox('what would you like to do', ("Draw number", "Train model", "Load model", "Upload number image", "Webscrape number image"))
    sidebar_1_options = {"Draw number": webdesign.draw_number, "Train model": models.train_model, "Upload number image": webdesign.upload_number_image, "Webscrape number image": scraper.number_image_scraper}
    sidebar_1_options.get(sidebar_1_selected_option)()

if __name__ == "__main__":
    main()


