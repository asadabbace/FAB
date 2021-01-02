import math
import pandas as pd
from datetime import datetime, timedelta
import time


class Helper:
    """class that is filled with a bunch of helper methods needed to run the bot"""

    def sig_fig(x: float, sig: int = 2) -> float:
        """ Rounds to the number of significant digits indicated"""
        return round(x, sig - math.ceil(math.log10(abs(x))))

    def string_to_timestamp(date: str) -> int:
        """Converts String of form DD-MM-YY into millisecond timestamp"""
        return int(time.mktime(datetime.strptime(date, "%d/%m/%Y").timetuple())) * 1000

    def into_dataframe(lst: list) -> pd.DataFrame:
        """Converts Binance response list into dataframe"""
        return pd.DataFrame(lst, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume",
                                          "Timestamp_end", "", "", "", "", ""]).set_index("Timestamp")

    def calculate_minute_disparity(df: pd.DataFrame, tf: int) -> float:
        """Calculates the difference (in minutes) of old the current dataframe is with respect to the live data"""
        # Getting the last date on your current dataset
        last_minute = df.iloc[-1]["Datetime"].to_pydatetime()
        current_minute = datetime.now()
        #     print(current_minute,last_minute, timedelta(minutes=tf))
        # Performing calculation to get the difference
        diff = (current_minute - last_minute - timedelta(minutes=tf)).seconds / 60
        return diff
