import streamlit as st
import pandas as pd
import requests

# Function to post the data to the API endpoint and get the response


def get_api_response(data):
    api_url = "https://api.andrewireland.co.uk/hotwater"
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()


# Streamlit app


def main():
    st.title("Hot Water | Energy Calculator")

    st.write("Please input the following variables:")

    # Input fields

    litres = st.number_input("Cylinder Volume (litres)", value=180)
    cold_temp = st.number_input("Cold Temperature (°C)", value=12)
    hot_temp = st.number_input("Hot Temperature (°C)", value=65)
    efficiency = st.number_input("Efficiency", value=1.0)
    heater_kW = st.number_input(
        "Heater Size (kW)", value=3.68)

    # Create a JSON object with the user-input data
    data = {
        "litres": litres,
        "cold_temp": cold_temp,
        "hot_temp": hot_temp,
        "efficiency": efficiency,
        "heater_kW": heater_kW,
    }

    if st.button("Submit"):
        # Get the API response
        api_response = get_api_response(data)

        # Display the figures in a card
        st.subheader("Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Cylinder Energy Storage (kWh)",
                    f"{api_response['kWh']:.2f}kWh")
        col2.metric("Heat Up Cost (Standard)",
                    f"£{api_response['costStandard']:.2f}")
        col3.metric("Heat Up Cost (Off Peak)",
                    f"£{api_response['costOffPeak']:.2f}")

        st.write(f" ")
        st.write(f" ")
        st.write(f"deltaT: {api_response['deltaT']:.2f}°C")
        st.write(
            f"Cylinder Energy Storage (kWh): {api_response['kWh']:.2f}kWh")
        st.write(f"Heat Up Time (hr): {api_response['heatUpTime']:.2f}")
        st.write(
            f"Heat Up Cost (Standard): £{api_response['costStandard']:.2f}")
        st.write(
            f"Heat Up Cost (Off Peak): £{api_response['costOffPeak']:.2f}")


if __name__ == "__main__":
    main()
