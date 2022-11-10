import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import pandas as pd
from itertools import count
def get_data():
    request = youtube_analytics.reports().query(
                    startDate='2021-04-24',
                    endDate='2022-11-11',
                    ids='channel==UCOwyfb8QhvvXQpoQLJpmEKQ',
                    dimensions= 'day',
                    metrics= 'views',
                    )
    response = request.execute()
    return response

def animate_youtube(i):
    x.append(last_30_days[i])
    y.append((last_30_views[i]))
    plt.xticks(rotation = 60)
    plt.plot(x,y, scaley=True, scalex=True, color="blue")

if __name__ == '__main__':
    scopes = ["https://www.googleapis.com/auth/yt-analytics.readonly"]
    client_secrets_file = "./oauth.json"
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube_analytics = googleapiclient.discovery.build('youtubeAnalytics', 'v2', credentials=credentials)
    data = get_data()
    date = []
    views = []
    for d in data['rows']:
        date.append(d[0].replace('2022-',''))
        views.append(d[1])
    last_30_days = date[-30:]
    last_30_views = views[-30:]


    try:
        os.mkdir("animation")
    except:
        print("Directory exists !")

    try:
        x,y= [], []
        plt.style.use("seaborn")
        fig = plt.figure(figsize=(10,5))

        axes = fig.add_subplot(1,1,1)
        # axes.set_ylim(0, 50)
        axes.set_xlim(0, 30)

        ani = FuncAnimation(fig=fig, func=animate_youtube, interval=200)
        ani.save("./animation/stats.gif")
    except:
        print("Create Plot Sucessfully !")


