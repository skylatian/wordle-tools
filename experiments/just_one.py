from combo_func import get_data

single_date = "2023-02-10"

data = get_data(single_date)

output = data

if output is None:
        output = "no data"
if '\n' not in output:
    output = "No Attempt Made"

print(output)