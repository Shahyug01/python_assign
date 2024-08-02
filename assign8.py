import pandas as pd
import matplotlib.pyplot as plt

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_total_cases_by_country(self):
        total_cases = self.df.groupby('Country').sum()['Confirmed']
        total_cases.plot(kind='bar', title='Total Confirmed Cases by Country')
        plt.savefig('total_cases_by_country.png')
        plt.show()

    def plot_total_deaths_by_country(self):
        total_deaths = self.df.groupby('Country').sum()['Deaths']
        total_deaths.plot(kind='bar', title='Total Deaths by Country')
        plt.savefig('total_deaths_by_country.png')
        plt.show()

    def plot_total_recovered_by_country(self):
        total_recovered = self.df.groupby('Country').sum()['Recovered']
        total_recovered.plot(kind='bar', title='Total Recovered Cases by Country')
        plt.savefig('total_recovered_by_country.png')
        plt.show()

    def plot_active_cases_by_country(self):
        active_cases = self.df.groupby('Country').sum()['Active']
        active_cases.plot(kind='bar', title='Active Cases by Country')
        plt.savefig('active_cases_by_country.png')
        plt.show()

    def plot_new_cases_by_country(self):
        new_cases = self.df.groupby('Country').sum()['New cases']
        new_cases.plot(kind='bar', title='New Cases by Country')
        plt.savefig('new_cases_by_country.png')
        plt.show()

    def plot_new_deaths_by_country(self):
        new_deaths = self.df.groupby('Country').sum()['New deaths']
        new_deaths.plot(kind='bar', title='New Deaths by Country')
        plt.savefig('new_deaths_by_country.png')
        plt.show()

    def plot_new_recovered_by_country(self):
        new_recovered = self.df.groupby('Country').sum()['New recovered']
        new_recovered.plot(kind='bar', title='New Recovered Cases by Country')
        plt.savefig('new_recovered_by_country.png')
        plt.show()

    def plot_deaths_per_100_cases(self):
        deaths_per_100_cases = self.df.groupby('Country').sum()['Deaths / 100 Cases']
        deaths_per_100_cases.plot(kind='bar', title='Deaths per 100 Cases by Country')
        plt.savefig('deaths_per_100_cases_by_country.png')
        plt.show()

    def plot_recovered_per_100_cases(self):
        recovered_per_100_cases = self.df.groupby('Country').sum()['Recovered / 100 Cases']
        recovered_per_100_cases.plot(kind='bar', title='Recovered per 100 Cases by Country')
        plt.savefig('recovered_per_100_cases_by_country.png')
        plt.show()

    def plot_deaths_per_100_recovered(self):
        deaths_per_100_recovered = self.df.groupby('Country').sum()['Deaths / 100 Recovered']
        deaths_per_100_recovered.plot(kind='bar', title='Deaths per 100 Recovered by Country')
        plt.savefig('deaths_per_100_recovered_by_country.png')
        plt.show()

    def plot_confirmed_last_week(self):
        confirmed_last_week = self.df.groupby('Country').sum()['Confirmed last week']
        confirmed_last_week.plot(kind='bar', title='Confirmed Cases Last Week by Country')
        plt.savefig('confirmed_last_week_by_country.png')
        plt.show()

    def plot_1_week_change(self):
        one_week_change = self.df.groupby('Country').sum()['1 week change']
        one_week_change.plot(kind='bar', title='1 Week Change in Confirmed Cases by Country')
        plt.savefig('1_week_change_by_country.png')
        plt.show()

    def plot_1_week_percent_increase(self):
        one_week_percent_increase = self.df.groupby('Country').sum()['1 week % increase']
        one_week_percent_increase.plot(kind='bar', title='1 Week % Increase in Confirmed Cases by Country')
        plt.savefig('1_week_percent_increase_by_country.png')
        plt.show()

# Main program
if __name__ == '__main__':
    file_path = 'clean_covid_data.csv'
    loader = DataLoader(file_path)
    df = loader.load_data()
    if df is not None:
        visualizer = DataVisualizer(df)
        visualizer.plot_total_cases_by_country()
        visualizer.plot_total_deaths_by_country()
        visualizer.plot_total_recovered_by_country()
        visualizer.plot_active_cases_by_country()
        visualizer.plot_new_cases_by_country()
        visualizer.plot_new_deaths_by_country()
        visualizer.plot_new_recovered_by_country()
        visualizer.plot_deaths_per_100_cases()
        visualizer.plot_recovered_per_100_cases()
        visualizer.plot_deaths_per_100_recovered()
        visualizer.plot_confirmed_last_week()
        visualizer.plot_1_week_change()
        visualizer.plot_1_week_percent_increase()