from common_tools.common_tools import (collect_ukranian_defenders_losses,
                                       collect_kremlin_data)

if __name__ == '__main__':
    print('Путін хуйло, підораха лайно!!!!')
    killed_defenders = collect_ukranian_defenders_losses()
    print(len(killed_defenders))

    kremlin_data = collect_kremlin_data()
    for item in list(kremlin_data.keys())[:10]:
        print(kremlin_data[item]['header'])