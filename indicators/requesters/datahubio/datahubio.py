import datapackage
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url = 'https://datahub.io/core/s-and-p-500/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)


def get_data():
    # to load only tabular data
    resources = package.resources
    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
            return data
