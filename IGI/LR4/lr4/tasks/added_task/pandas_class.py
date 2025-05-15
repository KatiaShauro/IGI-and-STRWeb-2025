import os
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# import pandas as pd
# from IPython.display import display
#
#
# class PandasClass:
#     def __init__(self):
#         self.name = "D:\\BSUIR\\2 курс\\4 sem\\ИГИ\\lr4\\tasks\\added_task\\light_spotify_dataset.csv"
#         self.cols = ['artist', 'song', 'Genre', 'Popularity', 'Positiveness']
#         self.df = pd.DataFrame()
#         self.music_series = pd.Series()
#
#     def read_data_frame(self):
#         self.df = pd.read_csv(self.name, usecols=self.cols)
#         display(self.df.head(10).style.background_gradient(subset=['Popularity', 'Positiveness'], cmap='YlOrRd'))
#         return
#
#     def make_series(self):
#         self.music_series = pd.read_csv(self.name, index_col=['song'])['Popularity']
#         display(self.music_series.head(15))
#         return
#
#
# # Создаем экземпляр и вызываем методы
# pc = PandasClass()
# pc.read_data_frame()
# pc.make_series()


class PandasClass:
    def __init__(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        self.name = os.path.join(project_dir, "light_spotify_dataset.csv")
        self.cols = ['artist', 'song', 'Genre', 'Popularity', 'Positiveness']
        self.df = pd.DataFrame()
        self.full_df = pd.DataFrame()
        self.music_series = pd.Series()
        self.popularity_threshold = 80


    def read_data_frame(self):
        self.df = pd.read_csv(self.name, usecols=self.cols)
        self.full_df = pd.read_csv(self.name)
        self.full_df.set_index('song', inplace=True)
        print(self.df.head(2000))


    def make_series(self):
        self.music_series = pd.read_csv(self.name, index_col=['song'])['Popularity']
        print(self.music_series)


    def get_by_index(self, index: int):
        print(self.full_df.iloc[index])


    def get_by_name(self, name: str):
        try:
            print(self.full_df.loc[name])
        except KeyError as e:
            print(f"[ERROR]: {e}. Can not find your song :(\n")


    def get_data_frame_info(self):
        print("\n\nBASE INFO")
        print(self.df.info)
        print("\n\n DF STATISTICS")
        print(self.df.describe(include='all'))
        print("\n\n SERIES STATISTICS")
        print(self.music_series.describe())

    def calculate_positivity_ratio(self):
        """
        Compares the average positivity of popular songs with the average positivity of all songs
        Returns how many times the positivity of popular songs is higher than the average
        """
        avg_positivity_all = self.df['Positiveness'].mean()
        #popular_songs = self.df[self.df['Popularity'] >= self.popularity_threshold]
        popular_songs = self.analyze_top_songs()
        avg_positivity_popular = popular_songs['Positiveness'].mean()

        if avg_positivity_all > 0:
            ratio = avg_positivity_popular / avg_positivity_all
            return round(ratio, 2)
        return 0


    def analyze_top_songs(self, n = 5):
        """Analysis of the top N most popular songs"""
        top_songs = self.df.nlargest(n, 'Popularity')
        return top_songs[['artist', 'song', 'Popularity', 'Positiveness']]


if __name__ == "__main__":
    p = PandasClass()
    p.read_data_frame()
    p.make_series()
    print(f"\n\n---SONG BY ID---\n")
    p.get_by_index(0)

    print(f"\n\n---SONG BY NAME---\n")
    p.get_by_name("Doubt")

    p.get_data_frame_info()

    print("\n\nTHE MOST POPULAR SONGS")
    print(p.analyze_top_songs(20))

    print(f"\n\nTHE POSITIVENESS RATIO BETWEEN THE MOST POPULAR SONGS AND ALL : "
          f"{p.calculate_positivity_ratio()}")
