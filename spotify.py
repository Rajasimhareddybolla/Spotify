from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from cs50 import SQL
import numpy as np
import matplotlib.pyplot as plt
db = SQL("sqlite:///spotify.db")
poly = PolynomialFeatures(degree= 3)
model = LinearRegression()

def plot_popularity():
    Very_Popular =db.execute("""
                          SELECT COUNT(*) FROM SPOTIFY_SONGS WHERE classification = 'Very Popular'
                          """)[0]
    Popular = db.execute("""
                          SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Popular'
                          """)[0]
    Moderately_Popular =db.execute("""
                          SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Moderately Popular'
                          """)[0]
    Less_Popular = db.execute("""
                          SELECT count(*) FROM SPOTIFY_SONGS WHERE classification = 'Less Popular'
                          """)[0]
    x_axis = np.array(["Very Popular",'Popular',"Moderately Popular","Less Popular"])
    y_axis = np.array([Very_Popular["COUNT(*)"],Popular["count(*)"],Moderately_Popular["count(*)"],Less_Popular["count(*)"]])
    plt.bar(x_axis,y_axis)
    plt.xlabel("popularity ")
    plt.ylabel("no of songs")
    plt.show()
def song_vs_year():
    data = db.execute("""
 SELECT count(*),year FROM SPOTIFY_SONGS GROUP BY year ORDER BY year ;
""")
    year = [x for x in range(1998,2021)]
    no_of_songs = [y["count(*)"] for y in data ]
    
    plt.scatter(year,no_of_songs)
    plt.xlabel("year")
    plt.ylabel("no of songs relesed")
    plt.show()
def predict_songs_per_year():
    data = db.execute("""
    SELECT count(*),year FROM SPOTIFY_SONGS GROUP BY year ORDER BY year ;
    """)
    year = np.array([x for x in range(1998,2021)])
    no_of_songs = [y["count(*)"] for y in data ]
    
    
    model.fit(year.reshape(-1,1),no_of_songs)
    plt.close()
    year_predd = np.array([x for x in range(1998,2030)])

    no_of_songs_pre = [model.predict(k.reshape(-1,1)) for k in year_predd]
    plt.scatter(year_predd,no_of_songs_pre,c="r")
    plt.scatter(year,no_of_songs)
    plt.xlabel("year")
    plt.ylabel("no of songs relesed")
    plt.show()
def predict():
    data = db.execute("""
    SELECT count(*),year FROM SPOTIFY_SONGS GROUP BY year ORDER BY year ;
    """)
    year = np.array([x for x in range(1999,2020)])
    no_of_songs = [y["count(*)"] for y in data ][1:-1]

    # Create a PolynomialFeatures object with degree 3
    poly = PolynomialFeatures(degree=3) # to convert that single var to polynomial 

    x_poly = poly.fit_transform(year.reshape(-1,1)) # now it convert and result the poly
    poly.fit(x_poly , no_of_songs)
    lin2 = LinearRegression()
    lin2.fit(x_poly , no_of_songs) # as we have polynomial feautures we can get no

    # Visualising the Linear Regression results
    plt.scatter(year, no_of_songs, color='blue')

    # Transform the year array for prediction
    year_poly_pred = poly.fit_transform(year.reshape(-1,1))
    plt.plot(year, lin2.predict(year_poly_pred), color='red')
    plt.title('Cubic Regression')
    plt.xlabel('Year')
    plt.ylabel('Number of Songs')

    plt.show()
def update(csv):
    
    # hear csv is the file path including the .csv from root lib
    db.execute(" .import ? --csv songs",csv)
# not enough data to implement
# def categories():
#     # Love songs: High valence, moderate energy, low loudness
#     if valence > 70 and energy > 50 and loudness < 60:
#         return "Love"
    
    
#     # Vibe songs: High valence, high energy, moderate loudness
#     elif valence > 60 and energy > 70 and loudness < 80:
#         return "Vibe"
    
#     # Mass songs: High energy, loudness, and valence
#     elif energy > 80 and loudness > 70 and valence > 80:
#         return "Mass"
    
#     # Chill songs: Low energy, low loudness, high instrumentalness
#     elif energy < 40 and loudness < 50 and instrumentalness > 70:
#         return "Chill"
    
#     # Party songs: High energy, high loudness, high speechiness
#     elif energy > 70 and loudness > 70 and speechiness > 60:
#         return "Party"
    
#     # Sad songs: Low valence, low energy, high speechiness
#     elif valence < 30 and energy < 40 and speechiness > 50:
#         return "Sad"
    
#     # Happy songs: High valence, high energy, high loudness
#     elif valence > 70 and energy > 60 and loudness > 70:
#         return "Happy"
    
#     # Relaxing songs: Low energy, moderate loudness, low speechiness
#     elif energy < 40 and loudness < 70 and speechiness < 30:
#         return "Relaxing"
    
#     # Other songs: Anything else
#     else:
#         return "Other"

predict()
