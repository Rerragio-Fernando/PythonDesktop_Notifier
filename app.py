from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Sample Notification", "Python is awesome!!!", duration=10, 
icon_path="Paomedia-Small-N-Flat-Bell.ico")