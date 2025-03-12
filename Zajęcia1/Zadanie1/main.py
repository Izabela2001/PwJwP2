from Zadanie1.mobile_app import MobileApp

app = MobileApp.import_data_from_json('data.json')
app.new_download()
print(MobileApp.total_downloads())