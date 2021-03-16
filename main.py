import requests
from twilio.rest import Client

Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "59380072eaeda154ef10c298240742f1"
my_lat = 47.376888
my_long = 8.541694

weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key
}

one_call = requests.get(Endpoint, params=weather_params)
one_call.raise_for_status()
data = one_call.json()
status_code = one_call.status_code
#sms section
account_sid = "ACf6fece104e06565ec1d2e2e9471d437a"
auth_token = "b06e91382820baa84f81897e18816768"
client = Client(account_sid, auth_token)

weather_slice = data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_number = hour_data["weather"][0]["id"]

    if int(condition_number) < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="Its going to rain today. Rememeber to bring an ☂️",
        from_="+18647124113",
        to="+27823956607"
    )
    print(message.status)
    # weather_data = []
    # for item in data["hourly"]:
    #     weather_data.append(item["weather"])
    #
    # rain = False
    # count = 0
    # for item in weather_data:
    #     count += 1
    #
    #     if count == 11:
    #         break
    #     else:
    #         condition = item[0]
    #         i_d = condition["id"]
    #
    #         if i_d < 700:
    #             rain = True
    # if rain:
    #     print("Bring an Umbrella")