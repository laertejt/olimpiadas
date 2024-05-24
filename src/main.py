import pandas as pd
import os
from pathlib import Path

def main():
    BASE_DIR = str(Path(os.path.dirname(__file__)).parent)
    file = BASE_DIR + '/data/athlete_events.csv'
    df = pd.read_csv(file)
    print(df.head(5))



if __name__ == '__main__':
    main()