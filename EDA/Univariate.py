class Univariate():
    def get_qual_quan(dataset):
        quan = []
        qual = []

        for column, dtype in dataset.dtypes.items():
            if dtype == object:
                qual.append(column)
            else:
                quan.append(column)

        return qual, quan