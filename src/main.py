import pandas as pd

from common_tools.common_tools import (collect_ukranian_defenders_losses,
                                       collect_ukr_president_data,
                                       collect_kremlin_data)


if __name__ == '__main__':
    print('Путін хуйло, підораха лайно!!!!')
    ukr_president = pd.DataFrame.from_dict(collect_ukr_president_data())
    print(ukr_president)

    killed_defenders = pd.DataFrame.from_dict(collect_ukranian_defenders_losses())
    print(killed_defenders)

    kremlin_data = pd.DataFrame.from_dict(collect_kremlin_data())
    print(kremlin_data)
