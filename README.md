# Design Document

By BOLLA RAJA SIMHA REDDY


## Scope


### Purpose of the Database

The main purpose of my database is two-fold:

1. **Optimizing Spotify Database Queries**: I aim to optimize the code accessing the Spotify database to retrieve data more efficiently. This optimization involves using indexes on frequently accessed columns, which can significantly speed up data retrieval operations.

2. **Data Visualization and Analysis**: I intend to visualize the data from the Spotify database using Python and Matplotlib. Data visualization provides insights and feedback, helping me make better inferences and further optimize my code. Additionally, visualization is crucial in the machine learning process to gain a deeper understanding of the data and improve optimization efforts.

#### Steps to Achieve These Purposes:

- **Database Indexing**: Identify frequently used columns in queries and create indexes on them to speed up data retrieval operations.

- **Query Optimization**: Analyze existing database queries for inefficiencies, refactor queries as needed, and ensure optimal use of indexes.

- **Data Visualization**: Develop Python scripts using Matplotlib to visualize data retrieved from the Spotify database. Create various types of visualizations such as histograms, scatter plots, and line plots to gain insights into different aspects of the data.

- **Feedback Loop**: Utilize insights gained from data visualization to iteratively improve database queries and optimization efforts. Visualizations help identify patterns, trends, and outliers that may not be apparent from raw data.

- **Machine Learning Integration**: Integrate machine learning algorithms into the analysis pipeline to further analyze and optimize Spotify database data. Machine learning techniques can identify correlations, predict future trends, and automate optimization tasks.

By following these steps, I aim to optimize database queries, gain insights through data visualization, and leverage machine learning for enhanced optimization efforts.  
### my database includes the following things :
1. **Artists**: Individuals or groups responsible for creating the songs stored in the database.
2. **Songs**: Individual musical compositions with associated metadata such as title, duration, popularity, etc.
3. **Musical Attributes**: Characteristics of songs such as energy, loudness, danceability, instrumentalness, etc., which describe the musical content.
4. **Genres**: Categories that classify songs based on stylistic characteristics and influences.
5. **Listeners**: Users who consume and interact with the music stored in the database.

* Which people, places, things, etc. are *outside* the scope of your database?

## Functional Requirements

### The user can use my database:

1. **Search Categories**: Users can search for songs based on genre, artist, album, release year, or song title.
   
2. **Access Popular Songs**: Users can find information about popular songs based on metrics such as popularity score or number of listens.

3. **Predict Music Trends**: Users can analyze historical data to predict trends in song popularity, genre classification, or user preferences.

4. **Personalized Recommendations**: Users can specify preferences to discover songs that match their taste in genre, mood, tempo, or artist.


* What's beyond the scope of what a user should be able to do with your database?

        
### Entities
1. **Main Entities**:
   - Songs, Artists, Genres, Users

2. **Attributes**:
   - Songs: Title, Duration, Year, Popularity, Genre
   - Artists: Name, Genre, Popularity
   - Genres: Name, Description
   - Users: Username, Email, Preferences

3. **Relationships**:
   - Songs belong to artists and genres.
   - Users create playlists with songs.
   - Users can rate songs or artists.

4. **Derived Attributes**:
   - Popularity of songs or artists could be calculated.

This provides a succinct overview of the entities, their attributes, relationships, and any derived attributes within your database.


### Relationships

![erd diagram](/images/raja.png)

## Optimizations

### Index Optimization Explanation

For optimal performance in our music app database, we have strategically created indexes on certain fields within the `SPOTIFY_SONGS` and `data` tables. These indexes are crucial for enhancing the efficiency of our data visualization and machine learning models. 

#### Indexes on `SPOTIFY_SONGS`

We have created an index named `spotify_songs_on_index` on the following fields:

- `id`: This is the primary key of the `SPOTIFY_SONGS` table, ensuring quick access to individual records.
- `Song`: This field allows rapid retrieval of songs based on their titles.
- `artist`: Indexing the artist field facilitates efficient querying for songs by specific artists.
- `genre`: Genre information is vital for various analytical tasks and recommendations.
- `classification`: Classification provides additional metadata that aids in data analysis and model training.

These indexes significantly improve the performance of data retrieval operations related to song information, which is fundamental for our data visualization efforts.

#### Indexes on `data`

Similarly, we have established an index named `on_data_index` on the following fields:

- `id`: The primary key of the `data` table, ensuring efficient access to individual records.
- `song_id`: This field links back to the `SPOTIFY_SONGS` table, facilitating joins and retrieval of detailed song data.
- `genere`: Genre information, as mentioned earlier, plays a pivotal role in our analyses and model training.
- `classification`: Classification metadata, like genre, contributes to the richness of our data and model training.

By optimizing these fields with indexes, we streamline the querying process for our machine learning algorithms, enabling faster training and more accurate predictions.

These index optimizations are tailored to the specific needs of our music app, focusing on enhancing performance where it matters most for data visualization and machine learning tasks.


## Limitations
 hear my data is limited to very small no such that it is difficult to optimise them for the good predictions in mechine learning models

 ## DATA VISUALISATION
 1) predict_songs_per_year() : 
        ![songs](/images/No_of_songs_prediction.png)  

 2) predict_songs_per_year() : 
        ![songs](/images/cubic.png)  
    
        gave the mechine learing model predictions for no of songs relesed vs year
 3) popularity() :  
        ![songs](/images/popularity.png)  
 4) update(csv):
  file csv file as an argument and update our database by adding the columns in that specified path